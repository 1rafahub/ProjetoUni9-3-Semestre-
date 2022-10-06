from flask import render_template, redirect, session, url_for
from config import app


@app.route('/')
def login():

    return render_template ('./login/login.html')

@app.route("/home")
def home():
    
    return render_template("./home/home.html")