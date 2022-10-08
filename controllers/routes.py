from flask import jsonify, render_template, redirect, session, url_for
from config import app
from connection import connection_db
import requests


@app.route("/home", methods = ['GET'])
def users():

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

