from . import db
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=30), nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(
        String(length=50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(
        String(length=65), nullable=False)
    budget: Mapped[int] = mapped_column(Integer(length=65), nullable=False)
    items = db.relationship('Item', backref="owned_user", lazy=True)


class Item(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(length=30), nullable=False, unique=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    barcode: Mapped[str] = mapped_column(
        String(length=12), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(
        String(length=1024), nullable=False, unique=True)
    owner: Mapped[int] = mapped_column(Integer, ForeignKey('user.id',))

    def __repr__(self) -> str:
        return f"item {self.name}"
