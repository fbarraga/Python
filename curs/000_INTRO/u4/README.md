# Entorns de desenvolupament i editors de texte

Una decisió important que has de prendre quan comences a treballar en programació és sobre l'editor o editors de texte que utilizaràs. Hi ha moltes opcions i aspectes a considerar. A més en determinats entorns es possible que no sigui suficient amb utilitzar un simple editor de texte i sigui necessari l'ús d'un ** IDE (entorn de desenvolupament integrat) **, que a més de la possibilitat d'editar el codi, ens ofereixi altres eines com: 

    * depuració de códi
    * generació automàtica de codi
    * ajuda integrada
    * gestió del projecte
    * gestió del control de versiones
    * ...

A l'hora de decidir en quin entorn treballar, ens haurem de fer les següents preguntes:

* ¿Editor gràfic o en consola? Per tasques d'administració lo ideal sería saber gestionar un editor de texte en consola, ja que moltes vegades hauràs de fer-ho en un equip remot sense entorn gràfic. Las tres opcions més habituals son:
  *  vim
  *  nano
  *  emacs-nox 
Per tasques de programació, es habitual es utilizar un editor gràfic amb més funcionalitats: emacs, atom, sublime text, notepad++

* ¿Editor simple o IDE?. S'hauria de considerar que aprendre a gestionar un IDE porta més temps que un simple editor i no és l'adequat per aplicacions senzilles com les que s'utilizen per aprendre un llenguatge. Evidentement l'us d'un IDE es fa imprescindible en un entorn professional.
* ¿Quines funcionalitats bàsiques haurà de tenir l'editor?: resaltat de sintaxis, numeració de linees, control d'indentació, gestió completa des de teclat
 Suport per python.
* ¿És multiplataforma?. Permet que el mateix editor de texte s'utilitzi en diferents sistemes operatius? pot ser un aspecte determinant per nosaltres?.

## IDE per Python

* [Entorns de desenvolupament per Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)

## Editors de texte per Python

* [Editors de texte per Python](https://wiki.python.org/moin/PythonEditors)



# Configuració de python amb Visual Studio Code

Hi ha dos IDEs que s'utilitzen per la majoria de programadors de Python:

  * [Pycharm](https://www.jetbrains.com/pycharm/)
  * [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)


Per la realització d'aquest curs utilitzarem Visual Studio Code. Podem trobar una guia de com configurar Python amb Visual Studio Code en aquest [link](https://code.visualstudio.com/docs/python/python-tutorial)


# Entorns virtuals

Entorns Virtuals ("virtualenvs") guarda les dependències (mòduls,...) del teu projecte separades del entorn global. T'ajuden a evitar conflictes de versions entre paquets i diferents versions del runtime de Python.

Abans de crear i activar un virtualenv podem mirar quin 'python' i 'pip' estem utilitzant per defecte al sistema:
    
    $ which python
    /usr/local/bin/python

## Creació d'un entorn virtual

Creem un virtualenv nou utilitzan la comanda de Python3:

    $ python3 -m venv ./venv

Un virtualenv és només un "entorn de Python en una carpeta":

    $ ls ./venv
    bin      include    lib      pyvenv.cfg


## Activació d'un entorn

L'activació d'un virtualenv configura la sessió actual de shell per utilitzar les comandes de python i pip  des de la carpeta del virtualenv en lloc de l'entorn global:

    $ source ./venv/bin/activate

Fixeu-vos com amb l'activació d'un virtualenv el prompt del shell del sistema canvia mostrant el nom de la carpeta virtualenv:

    (venv) $ echo "wee!"

Amb un virtualenv actiu, les comandes de 'python' s’executen a través del binari de python que hi ha en el virtualenv actiu:

    (venv) $ which python
    /Users/fbarragan/my-project/venv/bin/python3

Quan instal·lem noves llibreries i frameworks amb 'pip' s'instal·laran al *virtualenv sandbox*, deixant el teu entorn global  (i qualsevol altre virtualenvs) completament sense modificar:

    (venv) $ pip install requests

## Desactivació d'un entorn

Per tornar al Python global entorn, executeu la comanda següent:

    (venv) $ deactivate

Vegeu com ha canviat el prompt del sistema "normal" de nou?)

    $ echo "som-hi!"

Desactivant el virtualenv fa que el binari de `python` i `pip` tornin a utilitzar el global:

    $ which python
    /usr/local/bin/python


# Anaconda

Anaconda és una distribució del llenguatge Python i R per temes de for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), que intenta simplificar la gestió de paquets i el seu desplegament. La distribució conté paquets per Windows, Linux, and macOS.

Podeu trobar és informació a la web [www.anaconda.com](https://www.anaconda.com/)


***
[Index](../../../README.md)