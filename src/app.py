from flask import Flask

from src.routes import ticker

app = Flask(__name__)
app.register_blueprint(ticker.ticker)

if __name__ == '__main__':
    app.run(debug=True)