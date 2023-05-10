import os
from flask import Flask
from dotenv import load_dotenv
from account import account # import the account blueprint object
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

# register the blueprints with the app object
app.register_blueprint(account)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)