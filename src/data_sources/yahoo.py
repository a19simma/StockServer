import yfinance as yf

class YahooFinance():
    def getTicker(self, ticker):
        return yf.Ticker(ticker)


yahoo = YahooFinance()
msft = yahoo.getTicker('MSFT')

print(msft.history(period='max'))