from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from flask import current_app, has_app_context
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import DefaultMeta


Base = declarative_base(metaclass=DefaultMeta)

engines = {
    'pets': create_engine("sqlite:////tmp/pet.db"),
}


class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None):
        # mapper is None if someone tries to just get a connection
        if mapper is not None:
            info = getattr(mapper.mapped_table, 'info', {})
            bind_key = info.get('bind_key')
            if bind_key is not None:
                return engines[bind_key]
        return Session.get_bind(self, mapper, clause)


class DBObjectFlask(object):
    def __init__(self, configuration=None):
        db = SQLAlchemy(model_class=Base)
        db.init_app(current_app)

        self.session = db.session
        self.drop_all = db.drop_all
        self.create_all = db.create_all


class DBObjectPure(object):
    def __init__(self, configuration=None):
        self.engine = create_engine('sqlite:////tmp/test.db ')
        db_session = sessionmaker(bind=self.engine, class_=RoutingSession)
        session = scoped_session(db_session)
        Base.query = session.query_property()
        self.session = session
        self.tables = Base.metadata.tables

    def drop_all(self):
        Base.metadata.drop_all(self.engine, [self.tables['users']])
        Base.metadata.drop_all(engines['pets'], [self.tables['pets']])

    def create_all(self):
        Base.metadata.create_all(self.engine, [self.tables['users']])
        Base.metadata.create_all(engines['pets'], [self.tables['pets']])


def db_object_factory():
    if has_app_context():
        return DBObjectFlask()
    else:
        return DBObjectPure()


db = db_object_factory()
