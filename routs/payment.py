from pickle import FALSE

from flask import request, Blueprint
from middleware.middelware import getUserIdByToken
from services.account import hashingPassword
from services.payment import PaymentService
from services.user import UserService
cardRotesController = Blueprint("cardRotesController", __name__)

def checkIfEntitiesAreValid(data):

    # Remove all spaces in card number
    data['number'] = data['number'].replace(' ', '')

    # Check if number have valid len
    if len(data['number']) != 12 or len(data['month']) != 2 or len(data['year']) != 2 or len(data['CVV']) != 3:
        return False

    # Check if values contain only numbers
    try:
        data['number'] = int(data['number'])
        data['month'] = int(data['month'])
        data['year'] = int(data['year'])
        data['CVV'] = int(data['CVV'])
    except ValueError:
        return False

    # Check if month in valid range
    if data['month'] < 1 or data['month'] > 12:
        return False

    return True

class UserRoutesController:
    def __init__(self):
        self.Routes()

    def Routes(self):
        cardRotesController.add_url_rule('/getcards', view_func=self.getCards, methods=['GET'])
        cardRotesController.add_url_rule('/addcard', view_func=self.addCard, methods=['POST'])
        cardRotesController.add_url_rule('/updatecard', view_func=self.updateCard, methods=['PATCH'])
        cardRotesController.add_url_rule('/deletecard', view_func=self.deleteCard, methods=['DELETE'])

    # Rout for getting all Cards from DB
    def getCards(self):
        token = request.headers.get("token")

        userId = getUserIdByToken(token)
        userRole = PaymentService.checkUserRole(userId)

        if userRole != None and userRole == ('admin',):
            return PaymentService.getAllCards()

        return 'You are not Admin!'

    # Rout for adding new Card by User
    def addCard(self):
        newCard = request.get_json()
        token = request.headers.get("token")

        userId = getUserIdByToken(token)

        if 'number' and 'month' and 'year' and 'CVV' not in newCard.keys():
            return 'Invalid data request!'

        if type(newCard['number']) is not str and type(newCard['month']) is not str and type(newCard['year']) is not str and type(newCard['CVV']) is not str:
            return 'Invalid type of data request!'

        if checkIfEntitiesAreValid(newCard):
            return PaymentService.addNewCard(userId, newCard)

        return 'Invalid data request!'

    # Rout for updating User by User
    def updateCard(self):
        updateCard = request.get_json()
        token = request.headers.get("token")

        userId = getUserIdByToken(token)

        if type(updateCard['number']) is not str and type(updateCard['month']) is not str and type(updateCard['year']) is not str and type(updateCard['CVV']) is not str:
            return 'Invalid type of data request!'

        if checkIfEntitiesAreValid(updateCard):
            return PaymentService.updateCardByUserId(userId, updateCard)
        return 'Invalid data request!'

    # Rout for deleting User by User
    def deleteCard(self):
        token = request.headers.get("token")
        userId = getUserIdByToken(token)

        return PaymentService.deleteCardByUserId(userId)

UserRoutesController()

