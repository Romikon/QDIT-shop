from flask import request, Blueprint
from middleware.middelware import getUserIdByToken
from services.subscriptions import SubscriptionsService

subscriptionsRotesController = Blueprint("subscriptionsRotesController", __name__)


class SubscriptionsController:
    def __init__(self):
        self.Routes()

    def Routes(self):
        subscriptionsRotesController.add_url_rule('/getsubscriptions', view_func=self.getSubscriptions, methods=['GET'])
        subscriptionsRotesController.add_url_rule('/addsubscriptions/<brigadeId>', view_func=self.addSubscriptions,
                                                  methods=['POST'])
        subscriptionsRotesController.add_url_rule('/deletesubscriptions/<brigadeId>',
                                                  view_func=self.deleteSubscriptions, methods=['DELETE'])

    # Rout for getting all User Subscriptions from DB
    def getSubscriptions(self):
        token = request.headers.get("token")

        userId = getUserIdByToken(token)

        if userId != None:
            return SubscriptionsService.getAllSubscriptions(userId)

        return 'You need to log in!'

    # Rout for adding new Subscriptions by User
    def addSubscriptions(self, brigadeId):
        token = request.headers.get("token")

        userId = getUserIdByToken(token)

        if userId != None:
            return SubscriptionsService.addNewSubscriptions(userId, brigadeId)

        return 'You need to log in!'

    # Rout for deleting Subscriptions by User
    def deleteSubscriptions(self, brigadeId):
        token = request.headers.get("token")
        userId = getUserIdByToken(token)

        if userId != None:
            return SubscriptionsService.deleteSubscriptionsByUserId(userId, brigadeId)

        return 'You need to log in!'


SubscriptionsController()
