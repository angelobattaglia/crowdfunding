import sqlite3
import datetime

# Operations on comments

# I pass the id of the post and I get all the comments
def get_comments(id):
    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT commenti.id, commenti.data_pubblicazione, commenti.testo, commenti.valutazione, commenti.immagine_commento, commenti.id_utente, utenti.nickname, utenti.immagine_profilo FROM commenti LEFT JOIN utenti ON commenti.id_utente = utenti.id WHERE commenti.id_post = ?'
    cursor.execute(sql, (id,))
    comments = cursor.fetchall()

    cursor.close()
    conn.close()

    return comments

# I pass the the comment dictionary and I add the comment to the comments table on the DB
def add_comment(comment):
    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    success = False

    x = datetime.datetime.now()
    sql = 'INSERT INTO commenti(data_pubblicazione, testo, id_post, id_utente, Valutazione, immagine_commento) VALUES(?,?,?,?,?,?)'

    try:
        if comment['id_utente'] is None:
            cursor.execute(sql, (x.strftime("%Y-%m-%d"), comment['testo'], comment['id_post'], None , comment['Valutazione'], comment['immagine_commento']))
        else:
            cursor.execute(sql, (x.strftime("%Y-%m-%d"), comment['testo'], comment['id_post'], comment['id_utente'], comment['Valutazione'], comment['immagine_commento']))
        conn.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
        conn.rollback()
        success = False

    # cursor.execute(sql, (x.strftime("%Y-%m-%d"),
                         # comment['testo'], comment['id_post'], comment['id_utente'], comment['Valutazione'], comment['immagine_commento']))
    # conn.commit()
    # success = True
    # try:
        # conn.commit()
        # success = True
    # except Exception as e:
        # print('ERROR', str(e))
        # # if something goes wrong: rollback
        # conn.rollback()

    cursor.close()
    conn.close()

    return success