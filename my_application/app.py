from flask import Flask


def create_app():
    from my_application.db import db
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'pets':      'sqlite:////tmp/pet.db'
    }

    db = db.init_app(app)
    app.app_context().push()

    from my_application.modules.hello import hello_blueprint

    app.register_blueprint(hello_blueprint)
    return app, db


app, db = create_app()
