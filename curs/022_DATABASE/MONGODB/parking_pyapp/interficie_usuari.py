import platform  
import os

def netejar_pantalla():
    if platform.system() == 'Linux': os.system('clear')  
    if platform.system() == 'Windows': os.system('cls')

def mostrar_linia(n):  print('-' * n)

def mostrar_titol(a,b):  
    mostrar_linia(b)  
    print(f" {a}")  
    mostrar_linia(b)

def mostrar_menu(o):  
    mostrar_titol('MENU',30)
    for e in o:
        print(f" {e['numero']} · {e['text']}")
    mostrar_linia(30)
    opcio = input(' Opcio? ')
    return opcio

def mostrar_llista(ll):  
    for l in ll:
        print(' ' + l)  
    print()
