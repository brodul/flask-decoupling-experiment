from my_application.db import db


class Pet(db.Model):
    __bind_key__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Pet %r>' % self.username
