from my_application import db
from my_application.models.user import User
from my_application.models.pet import Pet

db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
pet = Pet(pet='pet')

db.session.add(admin)
db.session.add(pet)

db.session.commit()
