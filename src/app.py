from flask import Flask

from src.routes import ticker, company

app = Flask(__name__)
app.register_blueprint(ticker.ticker)
app.register_blueprint(company.company)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


application = app

if __name__ == '__main__':
    app.run(threaded=True, port="3000", host="0.0.0.0")
