from flask import Flask

from werkzeug.middleware.proxy_fix import ProxyFix

from src.routes import ticker, company

app = Flask(__name__)
app.register_blueprint(ticker.ticker)
app.register_blueprint(company.company)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0")
