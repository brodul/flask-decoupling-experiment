from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_BINDS'] = {
    'pets':      'sqlite:////tmp/pet.db'
}

db = SQLAlchemy(app)


from my_application.modules.hello import hello_blueprint

app.register_blueprint(hello_blueprint)
