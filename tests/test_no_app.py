from my_application.db_utils import db
from my_application.models.user import User
from my_application.models.pet import Pet


def test_db_object_type_pure(pure_database):
    from my_application.db_utils import DBObjectPure
    assert type(db) == DBObjectPure


def test_pet_exist(pure_database):
    pet = db.session.query(Pet).one()
    assert type(pet) == Pet
    assert pet.name == 'Tara'


def test_user_exist(pure_database):
    user = db.session.query(User).one()
    assert type(user) == User
    assert user.username == 'admin'


def test_pet_database(pure_database):
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:////tmp/pet.db')
    connection = engine.connect()
    assert len(engine.table_names()) == 1
    assert engine.table_names() == ['pets']
    result = connection.execute("select * from pets")
    assert result.first() == (1, 'Tara')
    connection.close()


def test_user_database(pure_database):
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    assert len(engine.table_names()) == 1
    assert engine.table_names() == ['users']
    result = connection.execute("select * from users")
    assert result.first() == (1, 'admin', 'admin@example.com')
    connection.close()
