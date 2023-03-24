import interficie_usuari as INUS  
import connector_postgresql as CONPO  
import persones as PER
import poblacions as POB  
import codis_postals as CP

opcions_menu = [
{'numero': '1', 'text': 'Llistar persones'},
{'numero': '2', 'text': 'Llister persones per patro als cognoms'},
{'numero': '3', 'text': 'Llistar poblacions'},
{'numero': '4', 'text': 'Obtenir telefon'},
{'numero': '5', 'text': 'Llistar codis postals'},
{'numero': '6', 'text': 'Afegir codi postal'},
{'numero': 'X', 'text': 'Sortir'}
]
#INUS.netejar_pantalla()
connexio = CONPO.establir_connexio()  
while True:
    opcio = INUS.mostrar_menu(opcions_menu)  
    print()

    if opcio == '1': 
        INUS.mostrar_llista(PER.llista_persones(connexio))  
    if opcio == '2':
        patro = input(' Patro? ')
        INUS.mostrar_llista(PER.llista_persones_patro_cog(connexio,patro))  
    if opcio == '3': 
        INUS.mostrar_llista(POB.llista_poblacions(connexio))  
    if opcio == '4':
        dni_tel = input(' DNI? ')
        INUS.mostrar_llista(PER.llista_tel_per(connexio,dni_tel))  
    if opcio == '5': 
        INUS.mostrar_llista(CP.llista_cp(connexio))  
    if opcio == '6':
        cod = input(' CP? ')
        pob = input(' Poblacio? ')  
        CP.afegir_cp(connexio,cod,pob)
    if opcio == 'X' or opcio == 'x': 
        break

CONPO.tancar_connexio(connexio)
