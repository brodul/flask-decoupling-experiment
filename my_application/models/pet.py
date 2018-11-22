from my_application.db_utils import Base
import sqlalchemy as sa


class Pet(Base):
    __tablename__ = 'pets'
    __bind_key__ = 'pets'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Pet %r>' % self.name
