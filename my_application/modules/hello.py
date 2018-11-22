from flask import Blueprint

from my_application.service.users import UsersService


hello_blueprint = Blueprint('hello_blueprint', __name__)


@hello_blueprint.route('/')
def hello_world():
    user_service = UsersService()
    return 'Hello, World! %s %s' % (hello_blueprint.name, user_service.get_first().username)
