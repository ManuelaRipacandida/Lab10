from database.DB_connect import DBConnect
from model.spedizione import Spedizione
from model.hub import Hub


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def readAllHub():
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Hub" # Query per prendere tutti gli hub
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor: # Creo oggetti Hub dal DB e li aggiungo alla lista
            hub = Hub(row["id"],
                      row["codice"],
                      row["nome"],
                      row["citta"],
                      row["stato"],
                      row["latitudine"],
                      row["longitudine"])
            result.append(hub)
        cursor.close()
        conn.close()
        return result  # Restituisco lista di oggetti hub (DTO)

    @staticmethod
    def readAllSpedizioni():
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM spedizione" # Prendo tutte le spedizioni

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)  # Parametro con (, )
        for row in cursor: # Creo oggetti Spedizione dal DB
            connessione = Spedizione(row["id"],
                                     row["id_compagnia"],
                                      row["numero_tracking"],
                                      row["id_hub_origine"],
                                      row["id_hub_destinazione"],
                                     row["data_ritiro_programmata"],
                                     row["distanza"],
                                     row["data_consegna"],
                                     row["valore_merce"])
            result.append(connessione)

        cursor.close()
        conn.close()
        return result # Lista di oggetti Spedizione




    @staticmethod
    def readGuadagnoMedio(id_hub_origine,id_hub_destinazione):
        conn = DBConnect.get_connection()
        result = []
        query = """SELECT AVG(valore_merce) AS valore_medio
        FROM spedizione
        WHERE 
            (id_hub_origine = %s AND id_hub_destinazione = %s)
            OR
            (id_hub_origine = %s AND id_hub_destinazione = %s)""" # Valore medio tra le due direzioni
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (id_hub_origine,id_hub_destinazione,id_hub_destinazione,id_hub_origine),)
        for row in cursor:
            result.append(row["valore_medio"]) # Salvo il valore medio
        cursor.close()
        conn.close()
        return result[0]  # La prima riga contiene il valore medio

