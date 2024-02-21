import sqlite3

# ------------------------------------------------
# ----------Adding Method(s)----------------------
# ------------------------------------------------
def add_raccolta(raccolta):
    # Connect to the SQLite database
    con = sqlite3.connect('data.db')
    # The following line configures the connection to return rows as dictionary-like objects. 
    # This allows accessing the columns of each row by names, 
    # making the code more readable and maintainable.
    con.row_factory = sqlite3.Row
    # Create a cursor object
    cur = con.cursor()

    # If an image is submitted, then the first SQL statement is executed, otherwise the second one is executed.
    if 'immagine_post' in raccolta:
        # the sql variable has its fields that have to corrispond to the fields of the database
        # the raccolta['date'], raccolta['text'], raccolta['immagine_post'], raccolta['id_utente'] are the fields of the dictionary post
        # hence these might not have the same name
        sql = 'INSERT INTO raccolte(nome_donazione, descrizione, immagine_donazione, obiettivo_monetario, capitale_donato, scadenza, id_utente) VALUES(?,?,?,?,?,?,?)'
        cur.execute(sql, (raccolta['nome_donazione'], raccolta['descrizione'], raccolta['immagine_donazione'], raccolta['obiettivo_monetario'], 
                          raccolta['capitale_donato'], raccolta['scadenza'], raccolta['id_utente']))
    else:
        sql = 'INSERT INTO raccolte(nome_donazione, descrizione, obiettivo_monetario, capitale_donato, scadenza, id_utente) VALUES(?,?,?,?,?,?)'
        cur.execute(sql, (raccolta['nome_donazione'], raccolta['descrizione'], raccolta['obiettivo_monetario'], 
                          raccolta['capitale_donato'], raccolta['scadenza'], raccolta['id_utente']))

    # This method is focused on verifying that the changes are committed to the database,
    # hence, it's a good practice to structure an if-then-else statement to handle the commit.
    try: 
        con.commit()
        success = True
    # In case of exception, the code rolls back the transaction to the last commit point.
    except Exception as e:
        print('ERROR', str(e))
        con.rollback()

    # Close the cursor and the connection
    cur.close()
    con.close()

    return success

# ------------------------------------------------
# -------------Fetching methods-------------------
# ------------------------------------------------
import sqlite3

def get_raccolte():
    conn = sqlite3.connect('data.db')
    # This line makes the rows returned by fetchall() to be in the form of dictionaries
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # SQL query to select all records from the "raccolte" table
    sql = 'SELECT * FROM raccolte'
    cursor.execute(sql)
    # Fetch all rows as a list of dictionaries
    raccolte = [dict(row) for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return raccolte

def get_raccolta(id):
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM raccolte WHERE id = ?'
    cursor.execute(sql, (id,))
    raccolta = cursor.fetchone()

    cursor.close()
    conn.close()

    return raccolta

def get_all_raccolte():
    # Connect to the SQLite database
    con = sqlite3.connect('data.db')

    # Set the row factory to sqlite3.Row for dictionary-like row objects
    con.row_factory = sqlite3.Row  

    # Create a cursor object
    cur = con.cursor()

    # Execute a SELECT query
    cur.execute('SELECT * FROM raccolte')

    # Fetch all the rows as dictionary objects
    # Ensure that row_objects is defined and used within the same scope
    row_objects = cur.fetchall()
    raccolte = [dict(row) for row in row_objects]  # Convert each row object to a dictionary

    # Close the cursor and the connection
    cur.close()
    con.close()

    return raccolte

# ------------------------------------------------
# -----------------Delete Method------------------
# ------------------------------------------------

import sqlite3

def delete_raccolta(id):
    # Connettersi al database SQLite
    con = sqlite3.connect('data.db')
    # Creare un oggetto cursore
    cur = con.cursor()

    # Definire la dichiarazione SQL DELETE. Il punto interrogativo (?) è un segnaposto per il valore di id.
    sql = 'DELETE FROM raccolte WHERE id = ?'

    # La variabile 'success' viene utilizzata per tracciare se l'operazione è stata eseguita con successo
    success = False

    try:
        # Eseguire la dichiarazione DELETE, passando l'id per sostituire il segnaposto
        cur.execute(sql, (id,))

        # Effettuare il commit delle modifiche al database
        con.commit()
        success = True
    except Exception as e:
        # In caso di eccezione, stampare l'errore e annullare tutte le modifiche
        print('ERRORE', str(e))
        con.rollback()
    finally:
        # Chiudere il cursore e la connessione
        cur.close()
        con.close()

    # Restituire lo stato di successo
    return success
