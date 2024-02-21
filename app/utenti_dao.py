import sqlite3

def add_user(user):

    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    success = False
    sql = 'INSERT INTO utenti(nickname, email, password) VALUES(?,?,?)'

    try:
        cursor.execute(
            sql, (user['nickname'], user['email'], user['password']))
        conn.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
        # if something goes wrong: rollback
        conn.rollback()

    cursor.close()
    conn.close()

def get_user_by_id(id):
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM utenti WHERE id = ?'
    cursor.execute(sql, (id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_email(email):
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM utenti WHERE email = ?'
    cursor.execute(sql, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_nickname(nickname):
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM utenti WHERE nickname = ?'
    cursor.execute(sql, (nickname,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_users():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT id, nickname, immagine_profilo FROM utenti'
    cursor.execute(sql)
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

