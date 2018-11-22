from my_application.models.user import User
from my_application.models.pet import Pet


def test_db_object_type(client, app_db):
    from my_application.db_utils import DBObjectFlask
    assert type(app_db) == DBObjectFlask


def test_pet_exist(client, app_db):
    pet = app_db.session.query(Pet).one()
    assert pet.name == 'Tara'


def test_user_exist(client, app_db):
    user = app_db.session.query(User).one()
    assert user.username == 'admin'


def test_pet_database_with_context(client):
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:////tmp/pet.db')
    connection = engine.connect()
    assert len(engine.table_names()) == 1
    assert engine.table_names() == ['pets']
    result = connection.execute("select * from pets")
    assert result.first() == (1, 'Tara')
    connection.close()


def test_user_database_with_context(client):
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    assert len(engine.table_names()) == 1
    assert engine.table_names() == ['users']
    result = connection.execute("select * from users")
    assert result.first() == (1, 'admin', 'admin@example.com')
    connection.close()
