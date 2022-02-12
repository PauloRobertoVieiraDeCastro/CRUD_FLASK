from modelo import*

SQL_DELETA_OLEO = 'DELETE from oleo where ide = %s'
SQL_OLEO_POR_ID = 'SELECT ide, Corrente, API, Nafta, Diesel, Gasoleo, Enxofre, Nitrogenio, TAN from oleo where ide = %s'
SQL_ATUALIZA_OLEO = 'UPDATE oleo SET Corrente=%s, API=%s, Nafta=%s, Diesel=%s, Gasoleo=%s, Enxofre=%s, Nitrogenio=%s, TAN=%s where ide = %s'
SQL_BUSCA_OLEO = 'SELECT ide, Corrente, API, Nafta, Diesel, Gasoleo, Enxofre, Nitrogenio, TAN from oleo order by Corrente asc'
SQL_CRIA_OLEO = 'INSERT into oleo (Corrente, API, Nafta, Diesel, Gasoleo, Enxofre, Nitrogenio, TAN) values (%s, %s, %s, %s, %s, %s, %s, %s)'

class DAO:
    def __init__(self, db):
        self.__db = db

    def salvar(self, oleo):
        cursor = self.__db.connection.cursor()
        if (oleo.ide):
            cursor.execute(SQL_ATUALIZA_OLEO, (oleo.corrente, oleo.api, oleo.nafta, oleo.diesel, oleo.gasoleo, oleo.s, oleo.n, oleo.tan, oleo.ide))
        else:
            cursor.execute(SQL_CRIA_OLEO, (oleo.corrente, oleo.api, oleo.nafta, oleo.diesel, oleo.gasoleo, oleo.s, oleo.n, oleo.tan))
            oleo.ide = cursor.lastrowid
        self.__db.connection.commit()
        return oleo

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_OLEO)
        oleos = traduz_oleos(cursor.fetchall())
        return oleos

    def busca_por_id(self, ide):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_OLEO_POR_ID, (ide,))
        tupla = cursor.fetchone()
        return Oleo(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], ide=tupla[0])

    def deletando(self, ide):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETA_OLEO, (ide,))
        self.__db.connection.commit()

def traduz_oleos(oleos):
    def cria_oleo_com_tupla(tupla):
        return Oleo(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], ide=tupla[0])
    return list(map(cria_oleo_com_tupla, oleos))    
    
