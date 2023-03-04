from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)


@app.route("/")
def pagina_inicial():
    return "Coded by Luiz Rioja 👽"


if __name__ == '__main__':  # pragma: no cover
    app.run()
