from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deployment"
DATABASE = Path(__file__).with_name("food_ordering.db")

FOOD_ITEMS = [
    {"id": 1, "name": "Margherita Pizza", "category": "Pizza", "price": 249, "description": "Classic cheese pizza with tomato sauce.", "emoji": "🍕"},
    {"id": 2, "name": "Veg Burger", "category": "Burger", "price": 129, "description": "Crispy vegetable patty with fresh lettuce.", "emoji": "🍔"},
    {"id": 3, "name": "Masala Dosa", "category": "South Indian", "price": 90, "description": "Golden dosa served with chutney and sambar.", "emoji": "🥞"},
    {"id": 4, "name": "Paneer Wrap", "category": "Wraps", "price": 159, "description": "Spiced paneer wrapped with crunchy vegetables.", "emoji": "🌯"},
    {"id": 5, "name": "French Fries", "category": "Sides", "price": 99, "description": "Crispy golden potato fries.", "emoji": "🍟"},
    {"id": 6, "name": "Chocolate Brownie", "category": "Dessert", "price": 110, "description": "Rich chocolate brownie.", "emoji": "🍫"},
]

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_db_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                items TEXT NOT NULL,
                total REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

@app.route("/")
def home():
    categories = sorted({item["category"] for item in FOOD_ITEMS})
    return render_template("index.html", foods=FOOD_ITEMS, categories=categories)

@app.route("/checkout", methods=["POST"])
def checkout():
    customer_name = request.form.get("customer_name", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()
    cart_json = request.form.get("cart_data", "")

    if not customer_name or len(customer_name) < 2:
        flash("Please enter a valid name.", "error")
        return redirect(url_for("home"))
    if not phone.isdigit() or len(phone) < 10 or len(phone) > 15:
        flash("Please enter a valid phone number (10–15 digits).", "error")
        return redirect(url_for("home"))
    if len(address) < 8:
        flash("Please enter a complete delivery address.", "error")
        return redirect(url_for("home"))

    import json
    try:
        submitted_items = json.loads(cart_json)
    except (json.JSONDecodeError, TypeError):
        submitted_items = []

    if not isinstance(submitted_items, list) or not submitted_items:
        flash("Your cart is empty. Please add food items first.", "error")
        return redirect(url_for("home"))

    food_lookup = {item["id"]: item for item in FOOD_ITEMS}
    order_lines = []
    total = 0
    for entry in submitted_items:
        try:
            food_id = int(entry.get("id"))
            quantity = int(entry.get("quantity"))
        except (AttributeError, TypeError, ValueError):
            continue
        if food_id not in food_lookup or quantity < 1 or quantity > 20:
            continue
        food = food_lookup[food_id]
        line_total = food["price"] * quantity
        total += line_total
        order_lines.append(f'{food["name"]} x {quantity} = ₹{line_total}')

    if not order_lines:
        flash("The cart does not contain valid items.", "error")
        return redirect(url_for("home"))

    with get_db_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO orders (customer_name, phone, address, items, total) VALUES (?, ?, ?, ?, ?)",
            (customer_name, phone, address, "\n".join(order_lines), total)
        )
        order_id = cursor.lastrowid

    return render_template("success.html", order_id=order_id, customer_name=customer_name,
                           order_lines=order_lines, total=total)

@app.route("/orders")
def orders():
    with get_db_connection() as connection:
        recent_orders = connection.execute(
            "SELECT id, customer_name, items, total, created_at FROM orders ORDER BY id DESC LIMIT 20"
        ).fetchall()
    return render_template("orders.html", orders=recent_orders)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
