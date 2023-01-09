
# Com crear executables en Python

Python és un popular llenguatge de programació utilitzat per molts desenvolupadors i organitzacions. De vegades és possible que hàgiu de fer executables independents a partir de l'script python, o crear executables amb dependències o convertir el fitxer python a exe. Això ajuda a fer que la vostra aplicació sigui portàtil a través de la plataforma Windows. Hi ha molts paquets python per ajudar-vos a aconseguir-ho. En aquest article, aprendrem a crear executables en Python mitjançant el mòdul [PyInstaller](https://pyinstaller.org/en/stable/).

Aquests són els passos per crear un fitxer executable en Python:

## Afegiu Python a PATH
Si Python no s'afegeix a Windows PATH, primer l'heu d'afegir. Podeu fer-ho fàcilment descarregant una última instal·lació de Python i marcant la casella de selecció "Afegeix Python a PATH" al començament de la instal·lació.

![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/pythoninstaller.png?raw=true)
 

## Obriu el command prompt

Obriu el símbol del Windows fent clic al botó d'inici i escrivint cmd a la caixa de cerca. Veureu "Indicador d'ordres" a la llista de suggeriments. Feu-hi clic per obrir l'indicador d'ordres a Windows.
 
![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/commandprompt.png?raw=true) 

## Instal·leu PyInstaller

El paquet PyInstaller inclou el vostre fitxer Python juntament amb les seves dependències en un executable. Instal·leu-lo amb l'ordre pip.

    $ pip install pyinstaller

## Create Python Script

Si encara no heu creat un script python, podeu crear-ne un amb un codi d'exemple dels que hem anat fent en aquest curs. Per seguir amb l'exemple utilitzarem myscript.py que ve detallat a continuació:

    import tkinter as tk

    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300)
    canvas1.pack()

    def hello ():  
        label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 200, window=label1)
    
    button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
    canvas1.create_window(150, 150, window=button1)

    root.mainloop()



## Creeu executables mitjançant PyInstaller

Ara que tenim PyInstaller instal·lat i el nostre script python a punt, continuarem amb la tasca de convertir-lo en executable. Aneu a la carpeta que conté el vostre script python myscript.py.

    C:\>cd C:\Users\fbarragan\Desktop\MyPython

A continuació, executeu l'ordre següent al vostre script python. Substituïu hello.py pel nom de l'script python.
        
        pyinstaller --onefile myscript.py


Recordeu utilitzar l'opció `--onefile` per convertir-lo en un sol fitxer .exe. En cas contrari PyInstaller crearà una carpeta de fitxers.

Bàsicament, quan executeu l'ordre anterior, pyinstaller analitzarà el vostre codi, esbrinarà les diverses biblioteques i paquets que necessita el vostre codi per executar-lo. Recollirà les còpies de tots aquests mòduls, inclòs el vostre intèrpret python i les posarà totes en un sol fitxer o carpeta, depenent de si utilitzeu l'opció -onefile o no.

Si realment teniu curiositat pel contingut de la vostra sortida de pyinstaller, creeu una còpia del vostre script python en una altra carpeta i crideu a pyinstaller en aquesta carpeta, sense l'opció -onefile. Veureu tots els fitxers i carpetes que Pyinstaller inclou a l'executable.

## Executar el .exe

Trobareu que PyInstaller va crear un fitxer .spec i 3 carpetes de compilació, dist i __pycache__ a la mateixa carpeta on es troba el vostre script python. Subcarpeta de boira oberta. En aquesta carpeta, trobareu el fitxer .exe amb el mateix nom de fitxer que el vostre script python, és a dir, `myscript.exe` en el nostre cas.

![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/distfolder.png?raw=true)
 
Podeu fer-hi doble clic per executar el vostre programa Python. En el nostre cas, veuràs la següent finestra amb el botó 'Click Me' que podràs clicar per veure el missatge 'Hola Món'. Si rebeu un missatge d'error, és possible que hàgiu d'instal·lar el [Visual C++ Redistributable](https://www.microsoft.com/es-ES/download/details.aspx?id=48145). Si el vostre script python no utilitza cap aplicació de Windows com tkinter, veureu la sortida en una finestra de consola.

És important tenir en compte que PyInstaller crearà un fitxer executable i no un instal·lador per al vostre fitxer Python. Si no utilitzeu l'opció -onefile, Pyinstaller crearà una llista de carpetes amb totes les dependències. Sigui com sigui, com que Pyinstaller inclourà l'intèrpret de Python i els mòduls necessaris per executar el vostre script python, la mida del vostre executable serà molt més gran que el vostre script python.
Un cop creat l'executable, és autodependent i portable a altres sistemes Windows. PyInstaller és una eina pràctica per crear fàcilment executables a partir de fitxers Python.

