from fastapi import APIRouter
from flask import request, Blueprint
from services.account import *

router = APIRouter()
accountRotesController = Blueprint("accountRotesController", __name__)

# Rout for authentication User
@accountRotesController.post('/authentication')
def authenticationCheck():
    User = request.get_json()
    if 'email' and 'password' not in User.keys():
        return 'Invalid data request!'
    if type(User['email']) is not str or type(User['password']) is not str:
        return 'Invalid type of data request!'

    return authentication(User)

# Rout for logging User
@accountRotesController.post('/login')
def loginCheck():
    User = request.get_json()
    if 'email' and 'password' not in User.keys():
        return 'Invalid data request!'
    if type(User['email']) is not str and type(User['password']) is not str:
        return 'Invalid type of data request!'

    return login(User)