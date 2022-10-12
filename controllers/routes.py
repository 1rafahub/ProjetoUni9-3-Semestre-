from flask import jsonify, render_template, redirect, session, url_for
from config import app
from connection import connection_db
import requests


@app.route("/home", methods = ['GET'])
def home():

    dados = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.tb_user")

    for row in cursor.fetchall():
        dados.append({
            "id": row[0],
            "id_user_type": row[1],
            "name": row[2],
            "email" : row[3],
            "telephone": row[4]
            })

    conn.close()

    return render_template("./home/home.html", dados = dados)

@app.route("/contratarservicos", methods = ['GET'])
def contratar_servicos():

    servicos = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
                    select tus.id_user_service, tus.id_type_service, tu.name, tu.email, tu.telephone, tus.activities, tus.hour_value from dbo.tb_user_services tus
                    left join dbo.tb_user tu on tus.id_user = tu.id_user
                    ''')


    for row in cursor.fetchall():
        servicos.append({
                        "id_user_service": row[0],
                        "id_type_service" : row[1],
                        "name" : row[2],
                        "email" : row[3],
                        "telephone" : row[4],
                        "activities": row[5],
                        "hour_value" : row[6]
                        })

    conn.close()

    return render_template("./contratar_servicos/contratar_servicos.html", servicos = servicos)

