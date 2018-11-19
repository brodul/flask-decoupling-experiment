from flask import Blueprint

from my_application import app, db
from my_application.models.user import User


hello_blueprint = Blueprint('hello_blueprint', __name__)


@hello_blueprint.route('/')
def hello_world():
    return 'Hello, World! %s %s' % (app.name, db.session.query(User).first().username)
