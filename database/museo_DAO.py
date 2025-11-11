from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass


    def trova_musei(self):
        cnx=ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM museo ORDER BY nome;")
        risultati = cursor.fetchall()

        musei=[]
        for row in risultati:
            musei.append(Museo(
                            id=row['id'],
                            nome=row['nome'],
                            tipologia=row["tipologia"]

                        )
            )
        cursor.close()
        cnx.close()
        return musei

