from dbconfig import cur, conn

class PaymentService:
    # Check if User is admin
    @staticmethod
    def checkUserRole(id):
        cur.execute("SELECT role FROM users WHERE id = %s", (id,))
        role = cur.fetchone()

        return role

    # Function for getting all Cards from DB
    @staticmethod
    def getAllCards():
        cur.execute("SELECT * FROM cards")
        allCards = cur.fetchall()

        return allCards

    # Function for adding new Card by User
    @staticmethod
    def addNewCard(userId, newCard):
        # Check if user already has card
        cur.execute("SELECT * FROM cards WHERE userid = %s", (userId,))
        Card = cur.fetchone()

        if Card is None:
            cur.execute(
                'INSERT INTO cards (userid, number, month, year, cvv) VALUES (%s, %s, %s, %s, %s)',
                (userId, newCard["number"], newCard["month"], newCard["year"], newCard["CVV"])
            )
            conn.commit()

            return "Card added successfully!"

        return 'You can only connect 1 card!'

    # Function for deleting Card by User
    @staticmethod
    def deleteCardByUserId(userId):
        # Check if card exist
        cur.execute("SELECT * FROM cards WHERE userId = %s", (userId,))
        Card = cur.fetchone()

        if Card != None:
            cur.execute('DELETE FROM cards WHERE userId = %s', (str(userId),))
            conn.commit()
            return "Card deleted successfully!"

        return "Card not found!"

    # Function for updating Card by User
    @staticmethod
    def updateCardByUserId(userId, updatedCard):
        # Check if card exist
        cur.execute("SELECT * FROM cards WHERE userid = %s", (userId,))
        Card = cur.fetchone()

        if Card != None:
            if updatedCard.get("number") is not None:
                cur.execute('UPDATE cards SET number = %s WHERE userId = %s', (updatedCard["number"], str(userId)))
            if updatedCard.get("month") is not None:
                cur.execute('UPDATE cards SET month = %s WHERE userId = %s', (updatedCard["month"], str(userId)))
            if updatedCard.get("year") is not None:
                cur.execute('UPDATE cards SET year = %s WHERE userId = %s', (updatedCard["year"], str(userId)))
            if updatedCard.get("CVV") is not None:
                cur.execute('UPDATE cards SET cvv = %s WHERE userId = %s', (updatedCard["CVV"], str(userId)))
            conn.commit()
            return "Card updated successfully!"

        return "Card not found!"
