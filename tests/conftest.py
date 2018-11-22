import pytest


@pytest.fixture(scope="module")
def client(app, app_db):
    from my_application.init_data import init_db

    client = app.test_client()

    app_db.drop_all()
    init_db(app_db)

    yield client
    app_db.drop_all()


@pytest.fixture(scope="module")
def app():
    from my_application.app import app
    app.config['TESTING'] = True
    return app


@pytest.fixture(scope="module")
def app_db(app):
    with app.app_context():
        from my_application.db_utils import db_object_factory
        db = db_object_factory()
    return db


@pytest.fixture(scope="module")
def pure_database():
    from my_application.init_data import init_db
    from my_application.db_utils import db

    db.drop_all()
    init_db(db)

    yield db
    db.drop_all()
