from dbconfig import cur, conn

class SubscriptionsService:
    # Function for getting all Cards from DB
    @staticmethod
    def getAllSubscriptions(userId):
        cur.execute("SELECT brigadesubscriptions FROM users WHERE id=%s", (str(userId),))
        allUserSubscriptions = cur.fetchall()

        return allUserSubscriptions

    # Function for adding new Card by User
    @staticmethod
    def addNewSubscriptions(userId, newSubscriptionId):
        # Fetch the current subscriptions
        cur.execute("SELECT brigadesubscriptions FROM users WHERE id = %s", (userId,))
        result = cur.fetchone()  # Use fetchone() to get a single row

        # Extract the current subscriptions array or initialize as an empty list
        subscriptions = result[0] if result and result[0] else []

        # Ensure the new subscription is not already in the list
        if newSubscriptionId not in subscriptions:
            subscriptions.append(newSubscriptionId)

        subscriptions = list(map(int, subscriptions))

        # Update the database with the updated subscriptions array
        cur.execute(
            "UPDATE users SET brigadesubscriptions = %s WHERE id = %s",
            (subscriptions, userId),
        )
        conn.commit()

        return "Subscriptions added successfully!"

    # Function for deleting Card by User
    @staticmethod
    def deleteSubscriptionsByUserId(userId, brigadeId):
        cur.execute("SELECT brigadesubscriptions FROM users WHERE id = %s", (userId,))
        result = cur.fetchone()

        subscriptions = result[0] if result and result[0] else []

        if int(brigadeId) in subscriptions:
            subscriptions.remove(int(brigadeId))

            cur.execute(
                "UPDATE users SET brigadesubscriptions = %s WHERE id = %s",
                (subscriptions, userId),
            )
            conn.commit()
            return "Subscription deleted successfully!"

        return "Subscription does not exist!"


