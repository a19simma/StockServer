from flask import Flask

from werkzeug.middleware.proxy_fix import ProxyFix

from src.routes import ticker, company

app = Flask(__name__)
app.register_blueprint(ticker.ticker)
app.register_blueprint(company.company)


@app.route("/")
def hello():
    html = "<h1>This is an api for stocks and economic data</h1>"
    html += "<p>Following are the endpoints available:<p>"
    html += "<ul>"
    for route in app.url_map.iter_rules():
        html += f'<li><a href="{route}">' + str(route) + "</code></li>"
        html = html.replace("<ticker>", "&lt;ticker&gt;")
        html = html.replace(
            '<li><a href="/static/<path:filename>">/static/<path:filename></code></li>', "")
    html += "</ul>"
    print(html)
    return html


app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0")
