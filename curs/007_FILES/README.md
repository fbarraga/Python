# Curs d'introducció a Python

## Introducció al sistema de fitxers

* Un **arxiu** o **fitxer** és un conjunt de bits que són emmagatzemats en un dispositiu. Als arxius informàtics se'ls anomena així perquè són els equivalents digitals dels arxius escrits en expedients, targetes, llibretes, paper o microfitxes de l'entorn d'oficina tradicional.

* Un **directori** és un contenidor virtual en què s'emmagatzemen una agrupació d'arxius informàtics i altres directoris, atenent al seu contingut, al seu propòsit o a qualsevol criteri que decideixi l'usuari.
Els arxius i directoris faciliten l'accés a la informació a partir de noms assignats arbitràriament.

Els directoris i fitxers s’organitzen jeràrquicament:


![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/jerarquiadirectorio.png?raw=true)


* Un camí o ruta és l'especificació de la localització d'un fitxer o directori:
    1. El **camí absolut** (o ruta absoluta) assenyala l’ubicació d'un arxiu  o directori des del directori arrel de sistema d'arxius.
    2. El **camí relatiu** (o camí relatiu) assenyala l’ubicació d'un arxiu o  directori a partir de la posició actual de sistema operatiu en el sistema d'arxius.

* El **sistema de fitxers** és el component del sistema operatiu  encarregat d'administrar i facilitar l'ús de les memòries perifèriques, ja siguin secundàries o terciàries. 
  
* Les seves principals funcions són l'assignació d'espai als arxius, l'administració de l'espai lliure i de l'accés a les dades emmagatzemades.

* Estructuren la informació emmagatzemada en un dispositiu d'emmagatzematge de dades o unitat d'emmagatzematge (normalment un disc dur d'un ordinador), que després serà representada ja sigui textual o gràficament utilitzant un gestor d'arxius.

![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/filesystem.png?raw=true)




Tots els sistemes operatius disposen d'una organització que és convenient conèixer perquè tots els fitxers que s'afegeixen a el sistema el fan respectant aquesta organització.
En els sistemes operatius GNU/Linux, afins i altres de la família Unix es segueix l'estàndard FHS (Filesystem Hierarchy Standard).En els sistemes operatius Windows l'organització respon a decisions arbitraries de Microsoft