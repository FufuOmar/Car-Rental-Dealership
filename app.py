from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
import sqlite3
import os

# Configure application
app = Flask(__name__)

db = SQL("sqlite:///cars.db")

cars = db.execute('SELECT * FROM cars')

app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/inventory', methods=["GET", "POST"])
def inventory():
    filter_cars = cars
    if request.method == "POST":
        color = request.form.get("color")
        style = request.form.get("style")
        type = request.form.get("type")

        # Base query
        query = "SELECT * FROM cars WHERE 1=1"
        parameters = []

        # Add conditions based on provided filters
        if color:
            query += " AND Color = ?"
            parameters.append(color)
        if style:
            query += " AND Style = ?"
            parameters.append(style)
        if type:
            query += " AND Type = ?"
            parameters.append(type)


        # Execute the query with parameters
        filter_cars = db.execute(query, *parameters)
    return render_template("inventory.html", cars=filter_cars)

@app.route('/rent/<int:car_id>', methods=["GET", "POST"])
def rent(car_id):
    car = db.execute("SELECT * FROM cars WHERE Id = ?", car_id)
    car_dict = dict(car[0])
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        startDate = request.form.get("startDate")
        returnDate = request.form.get("returnDate")
        phoneNum = request.form.get("phone")

        db.execute("INSERT INTO rents (first_name, last_name, email, phone, startDate, endDATE, car_id) VALUES (?, ?, ?, ?, ?, ?, ?)", firstName,
                    lastName, email, phoneNum, startDate, returnDate, car_id)

        flash(f"You sucessfully rented: {car_dict['Model']}!")

        return redirect("/my_rentals")

    return render_template("rent.html", car=car_dict)

@app.route('/my_rentals', methods=["GET", "POST"])
def myRentals():
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        phoneNum = request.form.get("phone")

        result = db.execute("SELECT car_id, startDate, endDATE FROM rents WHERE first_name = ? AND last_name = ? AND email = ? AND phone = ?",
                            firstName, lastName, email, phoneNum)
        result_dict = dict(result[0])
        if result:
            carID = result_dict['car_id']
            start_date = result_dict['startDate']
            end_date = result_dict['endDATE']
        car = db.execute("SELECT * FROM cars WHERE Id = ?", carID)
        car_dict = car[0]
        return render_template("view_rentals.html", car=car_dict, start_date=start_date, end_date=end_date)
    return render_template("my_rentals.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
