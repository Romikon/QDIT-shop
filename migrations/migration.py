from dbconfig import cur, conn

def dbMigrationUp():
    cur.execute("""CREATE TABLE users
        (
        id SERIAL PRIMARY KEY,
        email VARCHAR(20),
        password VARCHAR(200),
        role VARCHAR(20) DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    conn.commit()

def dbMigrationDown():
    cur.execute("""DROP TABLE users""")
    conn.commit()

#dbMigrationUp()
#dbMigrationDown()
