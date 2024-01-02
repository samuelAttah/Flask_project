from . import db, bcrypt, login_manager
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=30), nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(
        String(length=50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(
        String(length=65), nullable=False)
    budget: Mapped[int] = mapped_column(Integer, nullable=False, default=1000)
    items = db.relationship('Item', backref="owned_user", lazy=True)

    @property
    def password(self):
        raise AttributeError("Password is not a readable Attribute")

    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_password).decode('utf-8')

    def verify_password(self, plain_password):
        """returns a boolean"""
        return bcrypt.check_password_hash(self.password_hash, plain_password)


# Flask-Login's Callback function to load user given the user's ID
@login_manager.user_loader
def load_user(user_id):
    """Flask-Login's Callback function to load user given the user's ID. The user loader callback function receives a user identifier as a Unicode string. The
    return value of the function must be the user object if available or None otherwise."""
    return User.query.get(int(user_id))


class Item(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(length=30), nullable=False, unique=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    barcode: Mapped[str] = mapped_column(
        String(length=12), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(
        String(length=1024), nullable=False, unique=True)
    owner: Mapped[int] = mapped_column(
        Integer, ForeignKey('user.id'), default=1)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(name={self.name!r}, price={self.price!r}, barcode={self.barcode!r}, description={self.description!r}, owner={self.owner!r})"

    def __str__(self):
        return f"{self.name}"
