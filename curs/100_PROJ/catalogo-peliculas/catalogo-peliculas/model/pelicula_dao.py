from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicila[{self.nombre}, {self.duracion}, {self.genero}]'

def guadar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla peliculas no esta creado en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try: 
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro '
        mensaje = 'Crea la tabla en la Base de datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas 
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = 'Edición de datos'
        mensaje = 'No se apodido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
