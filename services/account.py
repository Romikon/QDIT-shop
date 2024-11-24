import binascii
from dbconfig import cur, conn
import bcrypt

from middleware.middelware import createToken


# Hashing password
def hashingPassword(password):
    bytes_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes_password, salt)
    return hash


# Compare two passwords
def checkPassword(userPassword, DBpassword):
    DBpassword = binascii.unhexlify(DBpassword[2:])
    userBytes = userPassword.encode('utf-8')
    result = bcrypt.checkpw(userBytes, DBpassword)

    return result


# Log in user
def login(userToCheck):
    cur.execute("SELECT * FROM users WHERE email = %s", (userToCheck["email"],))
    User = cur.fetchone()

    if User != None:
        if checkPassword(userToCheck["password"], User[2]):
            return createToken(User[0])
        else:
            return 'Invalid login or password!'

    return 'Invalid login or password!'


# authentication user
def authentication(newUsers):
    cur.execute("SELECT * FROM users WHERE email = %s", (newUsers['email'],))
    ifUserExist = cur.fetchone()
    if ifUserExist is not None:
        return 'User already exists!'

    newUsers['password'] = hashingPassword(newUsers['password'])

    cur.execute(
        'INSERT INTO users (email, password) VALUES (%s, %s)',
        (newUsers["email"], newUsers["password"])
    )
    conn.commit()
    return 'User added successfully!'
