# connector
import psycopg2

def establir_connexio():
    con = psycopg2.connect(host="localhost",dbname="agenda",  user="usag",  password="abcde")
    return con

def tancar_connexio(con):  
    con.close()
