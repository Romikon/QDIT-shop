from dbconfig import cur, conn

def dbMigrationUp():
    cur.execute("""CREATE TABLE users
        (
        id SERIAL PRIMARY KEY,
        email VARCHAR(20),
        password VARCHAR(200),
        role VARCHAR(20) DEFAULT 'user',
        brigadesubscriptions int ARRAY,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    cur.execute("""CREATE TABLE cards
            (
            id SERIAL PRIMARY KEY,
            userId INT,
            number varchar(16),
            month varchar(2),
            year varchar(2),
            CVV varchar(3),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (userId) REFERENCES users(id)
            )""")
    conn.commit()

def dbMigrationDown():
    cur.execute("""ALTER TABLE cards DROP CONSTRAINT cards_userId_fkey""")
    cur.execute("""DROP TABLE cards""")
    cur.execute("""DROP TABLE users""")
    conn.commit()

#dbMigrationUp()
#dbMigrationDown()
