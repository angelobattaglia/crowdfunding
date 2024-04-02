import sqlite3
# import random # need Random Strings that actually make sense

'''
    This file is used to populate the database with some test data. (TODO)
'''
def populate_raccolte():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Insert some records into the "utenti" table
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente001', 'nick001', 'email001@hello.com', 'password001'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente002', 'nick002', 'email002@hello.com', 'password002'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente003', 'nick003', 'email003@hello.com', 'password003'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente004', 'nick004', 'email004@hello.com', 'password004'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente005', 'nick005', 'email005@hello.com', 'password005'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente006', 'nick006', 'email006@hello.com', 'password006'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente007', 'nick007', 'email007@hello.com', 'password007'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente008', 'nick008', 'email008@hello.com', 'password008'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente009', 'nick009', 'email009@hello.com', 'password009'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente010', 'nick010', 'email010@hello.com', 'password0010'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente011', 'nick011', 'email011@hello.com', 'password0011'))
    # Insert some records into the "raccolte" table
    cursor.execute('INSERT INTO raccolte (nome, descrizione, data_creazione) VALUES (?, ?, ?)', ('Raccolta 1', 'Descrizione raccolta 1', '2021-01-01'))
    # Insert some records into the "donazioni" table
    cursor.execute('INSERT INTO donazioni (nome, descrizione, data_creazione) VALUES (?, ?, ?)', ('Raccolta 1', 'Descrizione raccolta 1', '2021-01-01'))

    conn.commit()
    conn.close()
