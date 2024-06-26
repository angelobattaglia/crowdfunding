# Creazione delle tabelle

Tabella utente con un'immagine impostata come predefinita

Sia "id" che "email" come chiave primaria. Questa chiave composita significa che il
la combinazione di "id" e "email" deve essere univoca in tutti i record. Anche se non è sbagliato avere un composito
chiave primaria, potrebbe essere più convenzionale avere solo la colonna "id" come chiave primaria, soprattutto se "id".
è destinato ad essere un identificatore univoco per ciascun utente. Puoi quindi imporre l'unicità della colonna "email".
attraverso un vincolo univoco se si vuole garantire che non possano registrarsi due utenti con lo stesso indirizzo email.

In questa versione, le colonne "nickname" e "password" sono definite come "TEXT". La colonna "email" ha un file unique
vincolo per garantire che gli indirizzi e-mail siano univoci per tutti gli utenti. La colonna "id" è l'unica chiave primaria,
rendendolo l'identificatore univoco per ciascun record nella tabella "utenti".

```sql
CREATE TABLE "utenti" (
    "id" INTEGER NOT NULL,
    "nickname" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
)
```

Se ho bisogno di eliminare una tabella, posso procedere come di seguito:
```sql
DROP TABLE "utenti"
```

Raccolte table with image set as default value if NULL
```sql
CREATE TABLE "raccolte" (

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
```

Donazioni table
```sql
CREATE TABLE "donazioni" (
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
```


## Alternatives

Other Alternatives for the same table:

- Using DATETIME for the start and ending Date
```sql
CREATE TABLE Fundraisers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Description TEXT,
    ImageURL TEXT, -- Assuming the image is stored elsewhere and accessed via a URL
    MonetaryGoal REAL NOT NULL,
    CollectionType TEXT CHECK(CollectionType IN ('flash', 'normal')) NOT NULL,
    StartTime DATETIME NOT NULL,
    EndTime DATETIME, -- EndTime can be calculated based on CollectionType, but storing it explicitly for 'normal' type
    MinDonation REAL NOT NULL CHECK(MinDonation >= 5), -- Assuming the minimum is 5 euros
    MaxDonation REAL NOT NULL CHECK(MaxDonation <= 5000) -- Assuming the maximum is 5000 euros

        -- La foreign key
    "id_utente"    INTEGER NOT NULL,
    FOREIGN KEY("id_utente") REFERENCES "utenti"("id")
);
```

- Using text fields for storing date and time values like StartTime and EndTime
```sql
CREATE TABLE Fundraisers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Description TEXT,
    ImageURL TEXT,
    MonetaryGoal REAL NOT NULL,
    CollectionType TEXT CHECK(CollectionType IN ('flash', 'normal')) NOT NULL,
    StartTime TEXT NOT NULL, -- Stored in ISO 8601 format 'YYYY-MM-DD HH:MM:SS'
    EndTime TEXT, -- Optional, depending on the CollectionType
    MinDonation REAL NOT NULL CHECK(MinDonation >= 5),
    MaxDonation REAL NOT NULL CHECK(MaxDonation <= 5000)

        -- La foreign key
    "id_utente"    INTEGER NOT NULL,
    FOREIGN KEY("id_utente") REFERENCES "utenti"("id")
);
```
