import yfinance as yf
class YahooFinance():
    def getTicker(self, ticker):
        ticker_object = yf.Ticker(ticker)        
        return ticker_object.history(period='max')
