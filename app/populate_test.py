import sqlite3
# import random # need Random Strings that actually make sense

'''
    This file is used to populate the database with some test data. (TODO)
'''
def populate_raccolte():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Insert some records into the "utenti" table
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente001', 'nick001', 'email001', 'password001'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente002', 'nick002', 'email002', 'password002'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente003', 'nick003', 'email003', 'password003'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente004', 'nick004', 'email004', 'password004'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente005', 'nick005', 'email005', 'password005'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente006', 'nick006', 'email006', 'password006'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente007', 'nick007', 'email007', 'password007'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente008', 'nick008', 'email008', 'password008'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente009', 'nick009', 'email009', 'password009'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente010', 'nick010', 'email010', 'password0010'))
    cursor.execute('INSERT INTO utenti (id, nickname, email, password) VALUES (?, ?, ?)', ('utente011', 'nick011', 'email011', 'password0011'))
    # Insert some records into the "raccolte" table
    cursor.execute('INSERT INTO raccolte (nome, descrizione, data_creazione) VALUES (?, ?, ?)', ('Raccolta 1', 'Descrizione raccolta 1', '2021-01-01'))
    # Insert some records into the "donazioni" table
    cursor.execute('INSERT INTO donazioni (nome, descrizione, data_creazione) VALUES (?, ?, ?)', ('Raccolta 1', 'Descrizione raccolta 1', '2021-01-01'))

    conn.commit()
    conn.close()
