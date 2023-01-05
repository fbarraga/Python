import sqlite3
import sys,os

class ConexionDB:
    def __init__(self):
        self.base_datos = 'database/peliculas.db'
        self.conexion = sqlite3.connect(os.path.join(sys.path[0],self.base_datos))
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()