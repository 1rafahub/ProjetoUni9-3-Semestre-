
from connection import connection_db

def get_faxineiros():   
    get_faxineiro = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
                    select tus.id_user_service, tus.id_type_service, tts.title, tu.name, tu.email, tu.telephone, tus.activities, tus.hour_value from dbo.tb_user_services tus
                    left join dbo.tb_user tu on tus.id_user = tu.id_user
                    left join dbo.tb_type_services tts on tus.id_type_service = tts.id_type_service
                    where tus.id_type_service = 1
                    ''')


    for row in cursor.fetchall():
        get_faxineiro.append({
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

    return get_faxineiro


def get_pedreiros():   
    get_pedreiros = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
                    select tus.id_user_service, tus.id_type_service, tts.title, tu.name, tu.email, tu.telephone, tus.activities, tus.hour_value from dbo.tb_user_services tus
                    left join dbo.tb_user tu on tus.id_user = tu.id_user
                    left join dbo.tb_type_services tts on tus.id_type_service = tts.id_type_service
                    where tus.id_type_service = 2
                    ''')


    for row in cursor.fetchall():
        get_pedreiros.append({
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

    return get_pedreiros

def get_eletricistas():   
    get_eletricistas = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
                    select tus.id_user_service, tus.id_type_service, tts.title, tu.name, tu.email, tu.telephone, tus.activities, tus.hour_value from dbo.tb_user_services tus
                    left join dbo.tb_user tu on tus.id_user = tu.id_user
                    left join dbo.tb_type_services tts on tus.id_type_service = tts.id_type_service
                    where tus.id_type_service = 3
                    ''')


    for row in cursor.fetchall():
        get_eletricistas.append({
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

    return get_eletricistas


def get_pintores():   
    get_pintores = []
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute('''
                    select tus.id_user_service, tus.id_type_service, tts.title, tu.name, tu.email, tu.telephone, tus.activities, tus.hour_value from dbo.tb_user_services tus
                    left join dbo.tb_user tu on tus.id_user = tu.id_user
                    left join dbo.tb_type_services tts on tus.id_type_service = tts.id_type_service
                    where tus.id_type_service = 4
                    ''')


    for row in cursor.fetchall():
        get_pintores.append({
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

    return get_pintores