# Run file to start the server

from flask import Flask
from dotenv import load_dotenv
import os

from routs.account import accountRotesController
from routs.user import userRotesController

load_dotenv()
app = Flask(os.getenv("NAME"))

app.register_blueprint(userRotesController)
app.register_blueprint(accountRotesController)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT"))