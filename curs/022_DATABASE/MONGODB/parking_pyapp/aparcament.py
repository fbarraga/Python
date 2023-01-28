import interficie_usuari as IU  
import base_de_dades as BDD  
import places
import historial

opcions_menu = [
    {'numero': '1', 'text': 'Llistar places'},
    {'numero': '2', 'text': 'Estat places'},
    {'numero': '3', 'text': 'Llistar historial'},
    {'numero': '4', 'text': 'Entrada vehicle'},
    {'numero': '5', 'text': 'Sortida vehicle'},
    {'numero': 'X', 'text': 'Sortir'}
]

#IU.netejar_pantalla()
connexio_bdd = BDD.establir_connexio()  
print(connexio_bdd)
bdd = BDD.seleccionar_bdd(connexio_bdd)  

while True:
    opcio = IU.mostrar_menu(opcions_menu)  
    print()
    if opcio == "1":
        print(" p id	grandaria")  
        IU.mostrar_llista(places.llistar(bdd))
    if opcio == "2":
        print(" id	estat")  
        IU.mostrar_llista(places.estat(bdd))
    if opcio == "3":  
        print(" historial")
        IU.mostrar_llista(historial.llistar(bdd))
    if opcio == "4":
        matricula = input("Matricula? ")  
        lloc = input("Plaça? ")  
        places.entrada(bdd,matricula,lloc)
    if opcio == "5":
        lloc = input("Plaça? ")  
        places.sortida(bdd,lloc)
        print(f"Preu: {historial.preu_a_pagar(bdd,lloc)}")  
    if opcio == "X" or opcio == "x": break

BDD.tancar_connexio(connexio_bdd)