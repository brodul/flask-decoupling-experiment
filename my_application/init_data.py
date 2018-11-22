from my_application.models.user import User
from my_application.models.pet import Pet


def init_db(db):

    db.create_all()

    admin = User(username='admin', email='admin@example.com')
    pet = Pet(name='Tara')

    db.session.add(admin)
    db.session.add(pet)

    db.session.commit()
