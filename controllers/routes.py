from flask import jsonify, render_template, redirect, session, url_for
from config import app
from connection import connection_db
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

    servicos = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
                    select tus.id_user_service, tus.id_type_service, tts.title, tu.name, tu.email, tu.telephone, tus.activities, tus.hour_value from dbo.tb_user_services tus
                    left join dbo.tb_user tu on tus.id_user = tu.id_user
                    left join dbo.tb_type_services tts on tus.id_type_service = tts.id_type_service
                    ''')


    for row in cursor.fetchall():
        servicos.append({
                        "id_user_service": row[0],
                        "id_type_service" : row[1],
                        "title" : row[2],
                        "name" : row[3],
                        "email" : row[4],
                        "telephone" : row[5],
                        "activities": row[6],
                        "hour_value" : row[7]
                        })

    conn.close()

    return render_template("./contratar_servicos/contratar_servicos.html", servicos = servicos)

@app.route("/contato")
def contato():
    return render_template("./contato/contato.html")

@app.route("/sobrenos")
def sobre_nos():
    return render_template("./sobre_nos/sobre_nos.html")