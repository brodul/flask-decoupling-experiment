import pytest

from my_application import app, db
from my_application.init_data import init_db


@pytest.fixture(scope="session")
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()

    yield client

    db.drop_all()
