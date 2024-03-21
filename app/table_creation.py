import sqlite3

def create_table_utenti():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "utenti" (
            "id" INTEGER NOT NULL,
            "nickname" TEXT NOT NULL,
            "email" TEXT NOT NULL UNIQUE,
            "password" TEXT NOT NULL,
            PRIMARY KEY("id")
        )
    ''')
    conn.commit()
    conn.close()

def create_table_raccolte():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "raccolte" (

            "id"    INTEGER PRIMARY KEY,

            -- Qui i campi che descrivono la raccolta
            "nome_donazione"    TEXT NOT NULL,
            "descrizione"    TEXT NOT NULL,
            "immagine_donazione"    TEXT DEFAULT 'img/default_image.png',

            -- Di seguito i campi che descrivono il lato monetario della raccolta
            "obiettivo_monetario" INTEGER NOT NULL,
            -- "capitale_donato" INTEGER, -- Could be NULL is nobody donates money -- I'll add this to the "donazioni" table

            -- Di che tipo di raccolta si tratta
            "CollectionType" TEXT CHECK(CollectionType IN ('flash', 'normal')) NOT NULL,

            -- E infine i campi che descrivono il carattere temporale della raccolta
            "StartTime"  INTEGER NOT NULL, -- Data in cui è stata postata la raccolta
            "EndTime"    INTEGER NOT NULL, -- I could count all in seconds from 14 days (1,210,000 seconds) to 5 minutes

            -- La foreign key
            "id_utente"    INTEGER NOT NULL,
            FOREIGN KEY("id_utente") REFERENCES "utenti"("id")
        );
    ''')
    conn.commit()
    conn.close()

def create_table_donazioni():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "donazioni" (
	        "id"	INTEGER NOT NULL,
	        "data"	INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
	        "nome"	TEXT NOT NULL, -- Questo campo è richiesto esplicitamente
	        "cognome"	TEXT NOT NULL, -- Questo campo è richiesto esplicitamente
	        "indirizzo"	TEXT NOT NULL, -- Questo campo è richiesto esplicitamente
	        "numero_carta"	TEXT NOT NULL, -- Questo campo è richiesto esplicitamente
	        "id_raccolta"	INTEGER NOT NULL,
	        -- "id_utente"	INTEGER, -- This can be null if it is Anonymous
	        -- "soldi_donati"	INTEGER CHECK ("soldi_donati" >= 1 AND "soldi_donati" <= 5000) NOT NULL,
	        "soldi_donati"	INTEGER CHECK ("soldi_donati" >= 1), -- It can be NULL, when the collection starts, or if it just doesn't receive any
	        PRIMARY KEY("id"),
	        -- FOREIGN KEY("id_utente") REFERENCES "utenti"("id"),
	        FOREIGN KEY("id_raccolta") REFERENCES "raccolte"("id")
        );
    ''')
    conn.commit()
    conn.close()
