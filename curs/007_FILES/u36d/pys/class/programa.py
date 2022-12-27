import sys
import os
import cotxe
import colleccio

opcio = sys.argv[1]
nom_fitxer = 'colleccio_cotxes.pckl'
colleccio_1 = colleccio.Colleccio()
num_cotxes = colleccio_1.carregar(nom_fitxer)

if opcio == '-l' and num_cotxes != 0:
    colleccio_1.mostrar()
if opcio == '-a':
    mat = input('Matricula? ')
    mar = input('Marca? ')
    mod = input('Model? ')
    col = input('Color? ')
    mot = input('Motor? ')
    ann = input('Any? ')
    nou_cotxe = cotxe.Cotxe(mat,mar,mod,col,mot,ann)
    colleccio_1.afegir(nou_cotxe)
    colleccio_1.emmagatzemar(nom_fitxer)
if opcio == '-d' and os.path.exists(nom_fitxer):
    os.remove(nom_fitxer)
if opcio == '-h':
    print('-l\tllistar\n-a\tafegir\n-d\tesborrar')
    print()