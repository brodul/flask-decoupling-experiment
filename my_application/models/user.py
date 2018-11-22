from my_application.db_utils import Base
import sqlalchemy as sa


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(80), unique=True, nullable=False)
    email = sa.Column(sa.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
