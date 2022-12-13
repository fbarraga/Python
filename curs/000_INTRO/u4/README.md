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
Per tasques de programació, es habitual es utilizar un editor gráfico con más funcionalidades: emacs, atom, sublime text, notepad++

* ¿Editor simple o IDE?. Habría que considerar que aprender a manejar un IDE lleva más tiempo que un simple editor y no es adecuado para aplicaciones sencillas como las que vamos a utilizar nosotros en este curso. Evidentemente el uso de un IDE se hace imprescindible en un entorno profesional.
* ¿Qué funcionalidades básicas debe tener el editor?: resaltado de sintaxis, numeración de líneas, control de sangrado (indentación), manejo completo desde teclado
 Soporte para python.
* ¿Es multiplataforma?. Permite que el mismo editor de texto se utilice en diferentes sistemas operativos y puede ser un aspecto determinante para nosotros.

## IDE per Python

* [Entorns de desenvolupament per Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)

## Editors de texte per Python

* [Editors de texte per Python](https://wiki.python.org/moin/PythonEditors)


# Entorns virtuals

Entorns Virtuals ("virtualenvs") guarda les dependències del teu projecte separades. T'ajuden a evitar conflictes de versions  entre paquets i diferents versions del runtime de Python.

Abans de crear i activar un virtualenv podem mirar quin 'python' i 'pip' estem utilitzant per defecte al sistema
 versió de l'intèrpret de Python
`$ which python`
/usr/local/bin/python

## Creació d'un entorn virtual

Creem un virtualenv nou utilitzan la comanda de Python3:

$ python3 -m venv ./venv

Un virtualenv és només un " entorn de Python en una carpeta":
$ ls ./venv
bin      include    lib      pyvenv.cfg


# Activació d'un entorn

L'activació d'un virtualenv configura la sessió actual de shell per utilitzar les comandes de python i pip  des de la carpeta del virtualenv en lloc de l'entorn global:

$ source ./venv/bin/activate

Fixeu-vos com amb l'activació d'un virtualenv el prompt del shell del sistema canvia mostrant el nom de la carpeta virtualenv:
(venv) $ echo "wee!"

Amb un virtualenv actiu, les comandes de 'python' s’executen a través del binari de python que hi ha en el virtualenv actiu*:

(venv) $ which python
/Users/dan/my-project/venv/bin/python3

Instal·lació de noves llibreries i frameworks amb 'pip' ara els instal·la al *virtualenv sandbox*, deixant el teu entorn global  (i qualsevol altre virtualenvs) completament sense modificar:
(venv) $ pip install requests

# Desactivació d'un entorn
Per tornar al Python global entorn, executeu la comanda següent:
(venv) $ deactivate

Vegeu com ha canviat el prompt del sistema "normal" de nou?)
$ echo "yay!"

# Deactivating the virtualenv flipped the
# `python` and `pip` commands back to
# the global environment:
$ which python
/usr/local/bin/python





***
[Index](../../../README.md)