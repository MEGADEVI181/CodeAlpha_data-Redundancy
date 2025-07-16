from flask import Flask, render_template_string, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("your_mongodb_connection_string")
db = client["bus_db"]
tickets = db["bookings"]

html = """
<h2>Book Bus Ticket</h2>
<form method='POST'>
Name: <input name='name'><br><br>
Route: <input name='route'><br><br>
Date: <input type='date' name='date'><br><br>
<input type='submit'>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        route = request.form["route"]
        date = request.form["date"]
        tickets.insert_one({"name": name, "route": route, "date": date})
        return "✅ Ticket Booked"
    return render_template_string(html)

app.run()
