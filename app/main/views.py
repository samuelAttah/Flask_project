from app.main import bp
from flask import render_template, redirect, url_for, flash, request
from app import db
from ..models import Item, User
from .forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


@bp.route('/')
def default_route():
    name = "Samuel"
    age = 70
    class_list = ["Samuel", "Kelly", "Drake", "Biden", "Bush", "Lincoln"]
    return render_template("index.html", my_name=name, my_age=age, my_list=class_list, title="Class List")


@bp.route('/home')
def home_route():
    return render_template('home.html')


@bp.route('/market', methods=['GET', 'POST'])
@login_required
def market_route():
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()

    if request.method == "POST":
        # Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        purchased_item_object = Item.query.filter_by(
            name=purchased_item).first()
        if purchased_item_object:
            if current_user.can_purchase(purchased_item_object):
                purchased_item_object.owner = current_user.id
                current_user.budget -= purchased_item_object.price
                db.session.commit()
                flash(
                    f"COngratulations! You purchased {purchased_item_object.name} for {purchased_item_object.price} ", category="success")
            else:
                flash(
                    f"Unfortunately, you don't have enough money to purchase {purchased_item_object.name}", category="danger")
        # Sell Item Logic
        sold_item = request.form.get('sold_item')
        sold_item_object = Item.query.filter_by(name=sold_item).first()
        if sold_item_object:
            if current_user.can_sell(sold_item_object):
                sold_item_object.owner = None
                current_user.budget += sold_item_object.price
                db.session.commit()
                flash(
                    f"COngratulations! You sold {sold_item_object.name} for {sold_item_object.price} ", category="success")
            else:
                flash(
                    f"Unfortunately, something went wrong with selling {sold_item_object.name}", category="danger")
        return redirect(url_for('main.market_route'))

    if request.method == "GET":
        # items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
        items = Item.query.filter_by(owner=None)
        user_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, sell_form=sell_form, user_items=user_items)


@bp.route('/register', methods=['GET', 'POST'])
def register_route():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email_address=form.email_address.data, password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(user=new_user)
        flash(
            f"Account created successfully!, You are now logged in as {new_user.username}", category='success')
        return redirect(url_for('main.market_route'))
    if len(form.errors) != 0:
        # print(f" type of errors {type(form.errors)}")
        for key, err in form.errors.items():
            flash(f"{key} error, Error message is {err[0]}", category="danger")
    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash(f"You are logged In as: {user.username}", category="success")
            return redirect(url_for('main.market_route'))
        flash("Invalid Username or Password", category='danger')
    return render_template('login.html', form=form)


@bp.route('/logout', methods=['GET'])
@login_required
def logout_route():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('main.home_route'))
