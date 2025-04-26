import sqlite3

users = sqlite3.connect('users.db')

cursor = users.cursor()
cursor.execute('''
     CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            password TEXT NOT NULL
    )
''')
users.commit()

def register_user(name, password):
    cursor.execute('''
        INSERT INTO users (name, password)
        VALUES (:name, :password)
    ''', (name, password))
    users.commit()

def login_user(name, password):
    cursor.execute('''
        SELECT * FROM users
        WHERE name = :name AND password = :password
    ''', (name, password))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False
