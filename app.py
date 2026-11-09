from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"

PRODUCTS = [
    {
        "id": 1,
        "name": "Футболка",
        "price": 2000,
        "image": "tshirt.jpg",
    },
    {
        "id": 2,
        "name": "Кроссовки",
        "price": 12000,
        "image": "sneakers.jpg",
    },
    {
        "id": 3,
        "name": "Олимпийка",
        "price": 2000,
        "image": "track-jacket.jpg",
    },
    {
        "id": 4,
        "name": "Свитер",
        "price": 3000,
        "image": "sweater.jpg",
    },
    {
        "id": 5,
        "name": "Рубашка",
        "price": 6000,
        "image": "shirt.jpg",
    },
    {
        "id": 6,
        "name": "Солнцезащитные очки",
        "price": 2000,
        "image": "sunglasses.jpg",
    },
    {
        "id": 7,
        "name": "Поло",
        "price": 5000,
        "image": "polo.jpg",
    },
    {
        "id": 8,
        "name": "Джинсы",
        "price": 5000,
        "image": "jeans.jpg",
    },
    {
        "id": 9,
        "name": "Брюки",
        "price": 8000,
        "image": "trousers.jpg",
    },
]


@app.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    print(session["cart"])
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.run(debug=True)
