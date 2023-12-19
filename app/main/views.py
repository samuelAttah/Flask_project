from app.main import bp
from flask import render_template
from app import db
from ..models import Item
from .forms import RegisterForm


@bp.route('/')
def default_route():
    name = "Samuel"
    age = 70
    class_list = ["Samuel", "Kelly", "Drake", "Biden", "Bush", "Lincoln"]
    return render_template("index.html", my_name=name, my_age=age, my_list=class_list, title="Class List")


@bp.route('/home')
def home_route():
    return render_template('home.html')


@bp.route('/market')
def market_route():
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
    return render_template('market.html', items=items)


@bp.route('/register')
def register_route():
    form = RegisterForm()
    return render_template('register.html', form=form)
