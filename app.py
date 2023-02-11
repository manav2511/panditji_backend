import sqlite3
import requests

# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import json

class Database:
    def __init__(self):
        self.conn = self.get_conn()
        self.cursor = self.conn.cursor()

    def get_conn(self):
        conn = sqlite3.connect("theist.db", timeout=15.0, check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        conn.row_factory = sqlite3.Row
        return conn

    def createUser(self, email, password, name, age, phone, gender, city, address):
        c = self.conn.cursor()

        c.execute("INSERT INTO users(email,password,name,age,phone,gender,city,address) VALUES (?,?,?,?,?,?,?,?);", (email,password,name,age,phone,gender,city,address))
        self.conn.commit()

    def createPandit(self, email, password, name, age, phone, city, about, rating, experience=0):
        c = self.conn.cursor()

        c.execute("INSERT INTO pandits(email,password,name,age,phone,experience,city,about,rating) VALUES (?,?,?,?,?,?,?,?);", (email,password,name,age,phone,experience,city,about,rating))
        self.conn.commit()

    def createBooking(self, user_id, service_id, date, pandit_id=1, transaction_id=1):
        c = self.conn.cursor()

        c.execute("INSERT INTO bookings(user_id, pandit_id, service_id, transaction_id, date) VALUES (?,?,?,?,?);", (user_id, pandit_id, service_id, transaction_id, date))
        self.conn.commit()

    def getUserByEmail(self, email):
        c = self.cursor()

        c.execute("SELECT * FROM users WHERE email = ?;", (email,))

        rows = c.fetchall()

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getService(self, id):
        c = self.cursor()

        c.execute("SELECT * FROM services WHERE id = ?", (id,))

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllServices(self, ):
        c = self.conn.cursor()

        c.execute("SELECT * FROM services;")
        
        rows = c.fetchall()

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllPandits(self, ):
        c = self.conn.cursor()

        c.execute("SELECT * FROM pandits;")
        
        rows = c.fetchall()

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllProducts(self, ):
        c = self.conn.cursor()

        c.execute("SELECT * FROM products;")
        
        rows = c.fetchall()

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllBookingsForUser(self, user_id):
        c = self.conn.cursor()

        c.execute("SELECT * FROM bookings WHERE user_id = ?;", (user_id,))
        
        rows = c.fetchall()

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllBookingsForPandit(self, pandit_id):
        c = self.conn.cursor()

        c.execute("SELECT * FROM bookings WHERE pandit_id = ?;", (pandit_id,))
        
        rows = c.fetchall()

        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllOrdersForUser(self, user_id):
        c = self.conn.cursor()

        c.execute("SELECT * FROM orders WHERE user_id = ?;", (user_id,))
        
        rows = c.fetchall()

        
        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    def getAllTransactionsForUser(self, user_id):
        c = self.conn.cursor()

        c.execute("SELECT * FROM transactions WHERE user_id = ?;", (user_id,))
        
        rows = c.fetchall()

        
        data = {"data": []}
        for r in rows:
            data["data"].append(dict(r))

        return data

    
    
# creating a Flask app
app = Flask(__name__)
database = Database()

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})

@app.route('/getAllPandits', methods = ['GET'])
def pandits():
    if(request.method == 'GET'):
        data = database.getAllPandits()
        return jsonify(data)

@app.route('/getAllProducts', methods = ['GET'])
def products():
    if(request.method == 'GET'):
        data = database.getAllProducts()
        return jsonify(data)

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

    return jsonify({'data': num**2})
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)