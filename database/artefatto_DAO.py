from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def trova_artefatto(self,museo_nome=None,epoca=None):
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query=""""SELECT a.id, a.nome, a.descrizione, a.epoca, m.nome AS museo_nome
            FROM artefatto a
            JOIN museo m ON a.id_museo = m.id"""

        condizioni=[]
        params=[]

        if museo is not None:
            condizioni.append("m.nome=%s")
            params.append(museo)

        if epoca is not None:
            condizioni.append("epoca=%s")
            params.append(epoca)

        if condizioni:
            query += " WHERE " + " AND ".join(condizioni)

        query += " ORDER BY a.nome"

        cursor.execute(query)
        result=cursor.fetchall()

        artefatti=[]
        for row in result:
            artefatti.append(Artefatto(
                                        id=row['id'],
                                        nome=row['nome'],
                                        tipologia=row['tipologia'],
                                        epoca=row['epoca'],
                                        museo_nome=row['museo_nome']))
        cursor.close()
        cnx.close()
        return artefatti

    def get_all_epoche(self):
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT epoca FROM artefatto ORDER BY epoca")
        epoche=[row[0] for row in cursor.fetchall()]
        cursor.close()
        cnx.close()
        return epoche









        
        
