from flask import request, Blueprint
from middleware.middelware import getUserIdByToken
from services.account import hashingPassword
from services.user import UserService

userRotesController = Blueprint("userRotesController", __name__)


class UserController:
    def __init__(self):
        self.Routes()

    def Routes(self):
        userRotesController.add_url_rule('/api/users', view_func=self.getUsers, methods=['GET'])
        userRotesController.add_url_rule('/api/users/<id>', view_func=self.getUsers, methods=['GET'])
        userRotesController.add_url_rule('/api/users', view_func=self.addUser, methods=['POST'])
        userRotesController.add_url_rule('/api/users/<id>', view_func=self.updateUser, methods=['PATCH'])
        userRotesController.add_url_rule('/api/users/<id>', view_func=self.deleteUser, methods=['DELETE'])

    # Rout for getting all Users from DB
    def getUsers(self):
        token = request.headers.get("token")

        userId = getUserIdByToken(token)
        userRole = UserService.checkUserRole(userId)

        if userRole != None and userRole == ('admin',):
            return UserService.getAllUsers()

        return 'You are not Admin!'

    # Rout for adding new User by admin
    def addUser(self):
        newUser = request.get_json()
        token = request.headers.get("token")

        userId = getUserIdByToken(token)
        userRole = UserService.checkUserRole(userId)
        if userRole != None and userRole == ('admin',):
            if 'email' and 'password' not in newUser.keys():
                return 'Invalid data request!'

            newUser['password'] = hashingPassword(newUser['password'])

            if type(newUser['email']) is not str and type(newUser['password']) is not str:
                return 'Invalid type of data request!'

            return UserService.addNewUser(newUser)

        return 'You are not Admin!'

    # Rout for updating User by admin
    def updateUser(self, id):
        updateUser = request.get_json()
        token = request.headers.get("token")

        userId = getUserIdByToken(token)
        userRole = UserService.checkUserRole(userId)

        if userRole != None and userRole == ('admin',):
            if type(updateUser['email']) is not str and type(updateUser['password']):
                return 'Invalid type of data request!'

            updateUser['password'] = hashingPassword(updateUser['password'])

            return UserService.updateUserById(id, updateUser)

        return 'You are not Admin!'

    # Rout for deleting User by admin
    def deleteUser(self, id):
        token = request.headers.get("token")

        userId = getUserIdByToken(token)
        userRole = UserService.checkUserRole(userId)

        if userRole != None and userRole == ('admin',):
            return UserService.deleteUserById(id)

        return 'You are not Admin!'


UserController()
