from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Магазин.</h1><a href='/cart'>Корзина</a>"


@app.route("/cart")
def cart():
    return "<h1>Ваша корзина</h1>" + "<section>Товары в корзине:</section>"

if __name__ == "__main__":
    app.run(debug=True)
