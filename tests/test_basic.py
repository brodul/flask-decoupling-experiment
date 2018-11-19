from my_application import db
from my_application.models.user import User
from my_application.models.pet import Pet


def test_pet_exist(client):
    db.session.query(Pet).one()


def test_user_exist(client):
    db.session.query(User).one()
