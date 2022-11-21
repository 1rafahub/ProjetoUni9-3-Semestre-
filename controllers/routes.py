from flask import render_template
from config import app
from connection import connection_db
from .controller_type_services import get_eletricistas, get_faxineiros, get_pedreiros, get_pintores
import requests
import json

@app.errorhandler(404) 
def not_found(e): 
  
  return render_template("./404/404.html") 

@app.errorhandler(500) 
def internal_error(e): 
  
  return render_template("./500/500.html") 


@app.route("/", methods = ['GET'])
def home():

    return render_template("./home/home.html")

@app.route("/contratarservicos", methods = ['GET'])
def contratar_servicos():

    eletricistas = get_eletricistas()

    faxineiros = get_faxineiros()

    pedreiros = get_pedreiros()

    pintores = get_pintores()


    return render_template("./contratar_servicos/contratar_servicos.html",
    eletricistas = eletricistas, 
    faxineiros = faxineiros,
    pedreiros = pedreiros,
    pintores = pintores
    )

@app.route("/contato")
def contato():
    return render_template("./contato/contato.html")

@app.route("/sobrenos")
def sobre_nos():
    return render_template("./sobre_nos/sobre_nos.html")