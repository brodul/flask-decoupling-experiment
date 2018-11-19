import pytest

from my_application.app import app
from my_application.init_data import init_db


@pytest.fixture(scope="session")
def client():
    from my_application.db import db

    app.config['TESTING'] = True
    client = app.test_client()

    db.drop_all()
    with app.app_context():
        init_db()

    yield client
