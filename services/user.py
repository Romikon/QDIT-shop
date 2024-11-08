from dbconfig import cur, conn

class UserService:
    # Check if User is admin
    @staticmethod
    def checkUserRole(id):
        cur.execute("SELECT role FROM users WHERE id = %s", (id,))
        role = cur.fetchone()

        return role

    # Function for getting all Users from DB
    @staticmethod
    def getAllUsers():
        cur.execute("SELECT * FROM users")
        allUsers = cur.fetchall()

        return allUsers

    # Function for adding new User by admin
    @staticmethod
    def addNewUser(newUser):
        cur.execute(
            'INSERT INTO users (email, password) VALUES (%s, %s)',
            (newUser["email"], newUser["password"])
        )
        conn.commit()

        return "User added successfully!"

    # Function for deleting User by admin
    @staticmethod
    def deleteUserById(id):
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        User = cur.fetchone()

        if User != None:
            cur.execute('DELETE FROM users WHERE id = %s', (str(id),))
            conn.commit()
            return "User deleted successfully!"

        return 'User does not exist!'

    # Function for updating User by admin
    @staticmethod
    def updateUserById(id, updatedUser):
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        User = cur.fetchone()

        if User != None:
            if updatedUser.get("email") is not None:
                cur.execute('UPDATE users SET email = %s WHERE id = %s', (updatedUser["email"], str(id)))
            if updatedUser.get("password") is not None:
                cur.execute('UPDATE users SET password = %s WHERE id = %s', (updatedUser["password"], str(id)))
            conn.commit()
            return "User updated successfully!"

        return 'User does not exist!'
