from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {
        "id": 1,
        "name": "Футболка",
        "price": 2000,
        "image": "images/tshirt.jpg",
    },
    {
        "id": 2,
        "name": "Кроссовки",
        "price": 12000,
        "image": "images/sneakers.jpg",
    },
    {
        "id": 3,
        "name": "Олимпийка",
        "price": 2000,
        "image": "images/track-jacket.jpg",
    },
    {
        "id": 4,
        "name": "Свитер",
        "price": 3000,
        "image": "images/sweater.jpg",
    },
    {
        "id": 5,
        "name": "Рубашка",
        "price": 6000,
        "image": "images/shirt.jpg",
    },
    {
        "id": 6,
        "name": "Солнцезащитные очки",
        "price": 2000,
        "image": "images/sunglasses.jpg",
    },
    {
        "id": 7,
        "name": "Поло",
        "price": 5000,
        "image": "images/polo.jpg",
    },
    {
        "id": 8,
        "name": "Джинсы",
        "price": 5000,
        "image": "images/jeans.jpg",
    },
    {
        "id": 9,
        "name": "Брюки",
        "price": 8000,
        "image": "images/trousers.jpg",
    },
]


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.run(debug=True)
