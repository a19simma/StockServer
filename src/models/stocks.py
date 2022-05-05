from ..database.connection import connection, cursor

class Stocks:
    def getAllTickers():
        query = 'SELECT ticker FROM stocks;'
        cursor.execute(query)
        return cursor.fetchall()
        
    def getByTicker(ticker):
        query = f'SELECT * FROM stocks WHERE ticker={ticker};'
        cursor.execute(query)
        return cursor.fetchall()

    def getByTicker(ticker, start, end):
        pass
        

