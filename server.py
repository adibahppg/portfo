#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:43:26 2021
A SERVER ACCEPTS A REQUEST FROM THE BROWSER
@author: adibahnurzainolabidin
"""

from flask import Flask, render_template, url_for, request, redirect #url_for==send_file
import csv #comes built-in with python
#use 'Flask' class to instantiate an 'app'
app = Flask(__name__)



@app.route("/")  #decorator
#anytime we hit '/' or route, I want you to define a function called 'Hello World'
def my_home():
    return render_template('index.html')
    #return "Hello, I'm Adibah the Astrochemist!"

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
               email = data["email"]
               subject = data["subject"]
               message = data["message"]
               file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
               email = data["email"]
               subject = data["subject"]
               message = data["message"]
               csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)               
               csv_writer.writerow(data.values()) #[]is to put things in a list



@app.route('/submit_form', methods=['POST', 'GET']) #get=browser wants us to send information; post = browser wants us to save information
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to database."
    else:
        return 'Something went wrong. Please try again!'

#@app.route("/favicon.ico")
#def favicon():
    #return send_file("static/favicon-16x16.png", mimetype='image/png')
#to run the application (from terminal)
# 1. export FLASK_APP=server.py #('server'- name of file)
# 2. flask run
# on terminal appears -
#WARNING: This is a development server. Do not use it in a production deployment. 
#Running on http://127.0.0.1:5000/ #LOCALHOST
## TO TURN ON THE DEBUG MODE
#$ export FLASK_ENV=development
#$ flask run

#@app.route("/about.html")
#def about():
    #return render_template('about.html')
    #return "Let's learn about the molecules in space!"

##ISN'T THIS A LITTLE TOO BASIC? WHAT CAN WE DO?##