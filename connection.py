import pyodbc 

def connection_db():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=BRCGHL2123;'
                        'Database=db_project_uni9;'
                        'Trusted_Connection=yes;')

    return conn
