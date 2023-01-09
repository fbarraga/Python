# Fitxer binaris

## pickle — Serialització d'objectes Python

El mòdul [pickle](https://docs.python.org/es/3/library/pickle.html) implementa protocols binaris per a serialitzar i deserialitzar una estructura d'objectes Python. «Pickling» és el procés mitjançant el qual una jerarquía d'objectes de Python es converteix en una seqüència de bytes, i el «unpickling» és l'operació inversa, mitjançant la qual una seqüència de bytes d'un fitxer binari (fitxer binari) o un. objecte tipus binari (objecte semblant a bytes) s'ha convertit novament en una jerarquía d'objectes. Pickling (y unpickling) son alternativamente coneguts com «serialización», «ensamblaje,» 1 o «aplanament»; sense embargo, per evitar confusions, els termes utilitzats aquí son «pickling» i «unpickling».


Format de flux de dades
El format de dades utilitzat per pickle és específic de Python. Això té la avantatge de que no hi ha restriccions impuestas per estàndards externs com JSON o XDR (que no poden representar l'ús compartit de punters); sense embargo, significa que els programes que no són de Python no poden ser capaços de reconstruir objectes Python serialitzats amb pickle.

Per defecte, el format de dades pickle utilitza una representació binària relativament compacta. Si necessiteu característiques de tamany òptimes, podeu comprar de manera eficient les dades serialitzades amb pickle.

El mòdul pickletools conté eines per analitzar els fluxos de dades generats per pickle. El código fuente de pickletools té comentaris extensos sobre els codis d'operació utilitzats pels protocols de pickle.

Actualment hi ha 6 protocols diferents que es poden utilitzar per serialitzar amb pickle. Quant major sea el protocol utilitzat, més recent serà la versió de Python necessària per llegir el pickle produït.

La versió 0 del protocol és el protocol original «legible para humans» i és compatible amb versions anteriors de Python.

La versió 1 del protocol és un format binari antic que també és compatible amb versions anteriors de Python.

La versió 2 del protocol es va introduir a Python 2.3. Proporciona un decapatge molt més eficient de les classes d'estil nou. Consulteu PEP 307 per obtenir informació sobre les millores aportades pel protocol 2.

S'agregó la versió 3 del protocol en Python 3.0. Teniu suport explícit per a objectes bytes i no es pot deserialitzar amb pickle per Python 2.x. Aquest era el protocol predeterminat en Python 3.0–3.7.

S'agregó la versió 4 del protocol en Python 3.4. Agrega suport per a objectes molt grans, pickling de més tipus d'objectes i algunes optimitzacions de format de dades. És el protocol predeterminat que comença amb Python 3.8. Consulteu PEP 3154 per obtenir informació sobre les millores aportades pel protocol 4.

S'agregó la versió 5 del protocol en Python 3.8. Agrega suport per a dades fora de banda i acceleració per a dades dins de banda. Consulteu PEP 574 per obtenir informació sobre les millores aportades pel protocol 5.

## Exemple de funcionament senzill

### Escriure un fitxer amb pickle

    >>> import pickle

    >>> llista = ['anna','lluis','pere','laura','maria','joan','manel','joan']
    >>> fitxer = open('dades.pckl','wb')
    >>> pickle.dump(llista,fitxer)
    >>> fitxer.close

    regular@debian:~$ ls
    escriure-dades-llista.py
    regular@debian:~$ python3 escriure-dades-llista.py
    regular@debian:~$ ls
    dades.pckl escriure-dades-llista.py
    regular@debian:~$ cat dades.pckl
    �]q(XannaqXlluisqXpereqXlauraqXmariaqXjoanqXmanelqhe.
    regular@debian:~$

Fixem-nos que a l'hora de fer el open del fitxer específiquem ('wb') això significa que obrim el fitxer en escriptura(w) y amb tipus binari.(b)

### Llegir un fitxer amb pickle

    >>> import pickle
    
    >>> fitxer = open('dades.pckl','rb')
    >>> llista = pickle.load(fitxer)
    >>> print(llista)
    >>> fitxer.close

    regular@debian:~$ ls
    dades.pckl escriure-dades-llista.py llegir-dades-llista.py
    regular@debian:~$ python3 llegir-dades-llista.py
    ['anna', 'lluis', 'pere', 'laura', 'maria', 'joan', 'manel', 'joan']
    regular@debian:~$

## Exemple llista amb diccionari

### Escriure dades d'una llista amb diccionari

    >>> import pickle
    
    >>> p1 = {'nom': 'eva', 'cognom': 'garcia'}
    >>> p2 = {'nom': 'anna', 'cognom': 'felip'}
    >>> p3 = {'nom': 'joan', 'cognom': 'garcia'}
    >>> p4 = {'nom': 'manel', 'cognom': 'lopez'}
    >>> ll = [p1,p2,p3,p4]
    >>> fitxer = open('dades.pckl','wb')
    >>> pickle.dump(ll,fitxer)
    >>> fitxer.close

    regular@debian:~$ ls
    escriure-dades-llis-dic.py
    regular@debian:~$ python3 escriure-dades-llis-dic.py
    regular@debian:~$ ls
    dades.pckl escriure-dades-llis-dic.py
    regular@debian:~$

### Llegir dades d'una llista amb diccionari

    >>> import pickle
    >>> fitxer = open('dades.pckl','rb')
    >>> ll = pickle.load(fitxer)
    >>> for e in ll:
            nom = e['nom']
            cognom = e['cognom']
            print(f"{cognom}, {nom}")
    >>> fitxer.close

    regular@debian:~$ ls
    dades.pckl escriure-dades-llis-dic.py llegir-dades-llis-dic.py
    regular@debian:~$ python3 llegir-dades-llis-dic.py
    garcia, eva
    felip, anna
    garcia, joan
    lopez, manel
    regular@debian:~$


## Exemple amb més d'un objecte

### Escriure més d'un objecte

    >>> import pickle
    >>> nom = 'joan'
    >>> cognoms = {'primer': 'garcia', 'segon': 'sanchez'}
    >>> edad = 27
    >>> notes = [{'mp01': 5.3}, {'mp02': 4.25}, {'mp03': 9.75}, {'mp04': 7.5}]
    >>> f = open('dad_per.pckl','wb')
    >>> pickle.dump(nom,f)
    >>> pickle.dump(cognoms,f)
    >>> pickle.dump(edad,f)
    >>> pickle.dump(notes,f)
    >>> f.close()

    regular@debian:~$ ls
    crear.py
    regular@debian:~$ python3 crear.py
    regular@debian:~$ ls
    crear.py dad_per.pckl
    regular@debian:~$

### Llegir més d'un objecte

    >>> import pickle
    >>> with open('d_per.pckl','rb') as f:
    >>> while True:
    >>>     try:
    >>>         obj = pickle.load(f)
    >>>         print(obj)
    >>>     except EOFError:
    >>>         break

    regular@debian:~$ ls
    crear.py dad_per.pckl llegir.py
    regular@debian:~$ python3 mostrar.py
    joan
    {'primer': 'garcia', 'segon': 'sanchez'}
    27
    [{'mp01': 5.3}, {'mp02': 4.25}, {'mp03': 9.75}, {'mp04': 7.5}]
    regular@debian:~$

## Exemple amb classes

* [Classe cotxe](./pys/class/cotxe.py)
* [Classe colleccio](./pys/class/colleccio.py)
* [Programa](./pys/class/escriure_class.py)


***
[Index](../../../README.md)

    