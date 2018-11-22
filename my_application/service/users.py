from my_application.db_utils import db
from my_application.models.user import User


class UsersService(object):
    """docstring for UsersService."""
    def __init__(self, db_session=None):
        self.session = db_session

    def get_first(self):
        return db.session.query(User).first()
