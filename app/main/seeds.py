from app.models import User
from app import db


def seed_users():

    users = [
        User(username="Franz", email_address="franz@springboard.com",
             password_hash="12345", budget=2500),
        User(username="Tim", email_address="tim@springboard.com",
             password_hash="12345", budget=2000),
    ]

    for user in users:
        db.session.add(user)

    db.session.commit()


if __name__ == "__main__":
    seed_users()
