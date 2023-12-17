# import os
# from app import create_app

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String, Integer, select
# from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
# from flask_wtf import FlaskForm
# from flask_migrate import Migrate
# # from apscheduler.schedulers.background import BackgroundScheduler

# # scheduler = BackgroundScheduler()

# app = Flask(__name__)


# class Base(DeclarativeBase):
#     pass


# db = SQLAlchemy(model_class=Base)

# # Configure the database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# # disable the feature of flask_sqlalchemy that signals the application everytime a change is about to be made in the database
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db.init_app(app)

# migrate = Migrate(app, db)


# class Item(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(
#         String(length=30), nullable=False, unique=True)
#     price: Mapped[int] = mapped_column(Integer, nullable=False)
#     barcode: Mapped[str] = mapped_column(
#         String(length=12), nullable=False, unique=True)
#     description: Mapped[str] = mapped_column(
#         String(length=1024), nullable=False, unique=True)

#     def __repr__(self) -> str:
#         return f"item {self.name}"


# # @app.before_first_request
# # def start_scheduler():
# #     scheduler.start()


# # @app.teardown_appcontext
# # def stop_scheduler(exception=None):
# #     scheduler.shutdown()

# with app.app_context():
#     db.create_all()

#     # db.session.add(Item(name="Gold", price=3000, barcode=1234,
#     #                description="A priceless piece of art that serves as a mineral resource"))

#     # db.session.add(Item(name="Silver", price=2500, barcode=4567,
#     #                description="Unique Shiny and underrated"))
#     # db.session.commit()

#     # items = db.session.execute(db.select(Item)).scalars()


# @app.route('/')
# def default_route():
#     name = "Samuel"
#     age = 70
#     class_list = ["Samuel", "Kelly", "Drake", "Biden", "Bush", "Lincoln"]
#     return render_template("index.html", my_name=name, my_age=age, my_list=class_list, title="Class List")


# @app.route('/home')
# def home_route():
#     return render_template('home.html')


# @app.route('/market')
# def market_route():
#     # items = [
#     #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#     #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#     #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
#     # ]
#     items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
#     return render_template('market.html', items=items)


# # def print_to_screen():
# #     print("This is my first attempt at Scheduling")


# # scheduler.add_job(print_to_screen, 'interval', seconds=5)
# # scheduler.start()


# if __name__ == '__main__':
#     app.run(debug=True)
