VERSION = "02"

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

## usual Flask initilization
app = Flask(__name__)

## DB declaration

# filename where to store stuff (sqlite is file-based)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


## define a table in the database

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    nickname = db.Column(db.String)


# actually create the database (i.e. tables etc)
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return f'hello, this is a chat app! (version {VERSION})'


# try it with
"""
http :5001/db/alive
"""
@app.route('/db/alive')
def db_alive():
    try:
        result = db.session.execute(text('SELECT 1'))
        print(result)
        return dict(status="healthy", message="Database connection is alive")
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


# try it with
"""
http :5001/api/version
"""
@app.route('/api/version')
def version():
    return dict(version=VERSION)


if __name__ == '__main__':
    app.run()
