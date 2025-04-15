VERSION = "01"

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


@app.route('/')
def hello_world():
    return f'hello, this is a chat app! (version {VERSION})'


if __name__ == '__main__':
    app.run()
