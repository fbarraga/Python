## El Llenguatge algorísmic

### Introducció

Un cop hem aprés a formalitzar l’enunciat d’un problema i a trobar la seva especificació, cal que siguem capaços de dissenyar l’algorisme que porta a la seva solució. L’eina bàsica de que disposem pel disseny d’algorismes és el *llenguatge algorísmic*.

Un llenguatge és un conjunt de símbols juntament amb un conjunt de regles **sintàctiques i semàntiques** que serveix per comunicar-nos.

Les regles sintàctiques determinen com s’han de combinar els símbols per fer construccions que pertanyin al llenguatge (com s’han de dir les coses). Per exemple, una oració consta de subjecte, predicat i complements.

Les regles semàntiques determinen quin és el significat de les construccions del llenguatge (què es diu).

El llenguatge que fem servir habitualment (català, castellà) s’anomena llenguatge natural. El llenguatge natural no és adient per expressar els  algorismes  perquè poden  arribar a  ser  molt  complicats  i  difícils d’entendre, ja que:

    * És massa complex (amb un subconjunt molt reduit n’hi hauria prou)
    * És ambigüu (per això tots els traductors automàtics entre diferents idiomes donen resultats tan poc satisfactoris)
    * Pot haver tantes formes d’expressar un algorisme en llenguatge natural com persones.

Al llarg del temps s’han proposat llenguatges alternatius que tenien com a objectiu la claredat, la simplicitat i la precisió: **els llenguatges formals**.

Nosaltres farem servir un llenguatge algorísmic que s’acostuma a fer servir molt sovint en la docència de la programació. La llista següent recull algunes de les característiques més rellevants del llenguatge algorísmic que farem servir:

    * És un llenguatge **simple** (té molts pocs elements i poques regles que recordar).
    * És un llenguatge **no ambigüu** (les seves construccions tenen un significat clar i precís).
    * És un llenguatge **potent**. Malgrat la seva simplicitat, permet expressar algorismes complexos.
    * Està destinat a interlocutors humans. Per tant, pot ser executat per qualsevol persona.
    * Per executar-lo en un computador, prèviament hem de codificar-lo en un llenguatge de programació.
    * La major part de construccions del llenguatge fan servir un reduit conjunt de paraules en català (com ara **algorisme**, **var**, **si**, **mentre**, etc.).

### Estructura genèrica d’un algorisme

Tots els algorismes comparteixen un patró comú que es descriu a continuació i que anirem ampliant a mesura que avancem en el temari:

        algorisme Nom de l’Algorisme

            const
            {Definició de constants} 
            fconst

            tipus
            {Definició de tipus} 
            ftipus

            var
            {Declaració de variables}
            fvar

            {Acció 1} 
            {Acció 2}
            {Acció 3}

            ...

        falgorisme

Comentaris

    * El llenguatge fa servir algunes paraules clau, com ara **algorisme** i **tipus.** Aquestes paraules clau les escriurem en **negreta** (a la pissarra, les subratllarem) per facilitar la lectura de l’algorisme i per distingir-les dels noms de les variables.
    * Tot algorisme comença per la paraula **algorisme** i acaba amb la paraula **falgorisme** (la f vol dir fi de l’algorisme).
    * El primer que segueix és la **definició de les constants** que farem servir a l’algorisme.
    * Després segueix la **definició dels tipus de dades** que farem servir a l’algorisme.
    * Després segueix la **declaració de les variables** que farem servir a l’algorisme.
    * Finalment, vé la part més important de l’algorisme: una succesió d’accions, que són les que modificaran els valors de les variables que hem declarat de cara a obtenir els resultats desitjats.

**Exemple: Càlcul de la lletra del NIF**

Especificació:

dni: **enter**;**      lletra: **caracter**

{Pre: dni=DNI **i** DNI>0}

calcul\_lletra\_NIF

{Post: lletra = la lletra que correspon a DNI}

Algorisme

    algorisme calcul\_lletra\_NIF

        const
        NUMLLETRES: enter = 23
        fconst

        var
        dni, codi: enter
        lletra: caracter
        fvar

        dni:=LlegirEnter()
        {dni=DNI i DNI>0}
        codi:= dni mod NUMLLETRES
        si
            codi=0 lletra:='T'
            codi=1 lletra:='R'
            codi=2 lletra:='W'
            codi=3 lletra:='A'
            codi=4 lletra:='G'
            codi=5 lletra:='M'
            codi=6 lletra:='Y'
            codi=7 lletra:='F'
            codi=8 lletra:='P'
            codi=9 lletra:='D'
            codi=10 lletra:='X'
            codi=11 lletra:='B'
            codi=12 lletra:='N'
            codi=13 lletra:='J'
            codi=14 lletra:='Z'
            codi=15 lletra:='S'
            codi=16 lletra:='Q'
            codi=17 lletra:='V'
            codi=18 lletra:='H'
            codi=19 lletra:='L'
            codi=20 lletra:='C'
            codi=21 lletra:='K'
            codi=22 lletra:='E'
        fsi

        {lletra = lletra que correspon a DNI} EscriuCaracter(lletra)

falgorisme

**Exemple: Càlcul del factorial d’un enter** 

Especificació:

n: **enter**

{Pre: n=N **i** N>=0} factorial

{Post: fact=N!}

Algorisme

    algorisme factorial

        var
        n, fact, i: enter
        fvar 
        n:=LlegirEnter() {n=N i N>=0} fact:=1
        i:=2

        mentre i<=n fer fact:=fact\*i
            i:=i+1
        fmentre
        {fact=N!}

        EscriureEnter(fact) 
    falgorisme

Més comentaris...

* El llenguatge fa servir una notació *parentitzada*: algunes paraules claus (com ara **var** i **fvar**) actuen com parèntesis en el sentit que serveixen per agrupar diferents parts de l’algorisme. Per exemple, **var** indica que comença l’apartat de definicions de variables, i **fvar** indica la fi d’aquest apartat. D’alguna forma, **var** actua com un parèntesi que s’obre, i **fvar** actua com un parèntesi que es tanca.

* Fixeu-vos  que  cada  cop  que  comença  un  nou  bloc  (amb  **var**,  **const**,  **mentre**,  etc.) augmentem la indentació del text (és a dir, la distància al marge esquerre); simètricament, cada  cop  que  acaba  un  bloc  (amb  **fvar**,  **fconst**,  **fmentre**,  etc.)  disminuim  un  nivell  la indentació. D’aquesta manera és molt més fàcil identificar on comencen i on acaben els diferents blocs de l’algorisme de forma visual.

## Variables, constants i tipus de dades

**Variable**: Una variable és un nom simbòlic associat a una determinada cel·la de memòria en la que es pot guardar un cert valor per recuperar-lo més endavant.

Als exemples anteriors, *dni, codi, fact* i *lletra* són variables.

**Constant**: Una constant és exactament el mateix que una variable de la qual no es permet alterar el seu contingut, és a dir, manté sempre el seu valor.

Exemples de constants són PI, E, VELOCITAT\_LLUM.

També reben el nom de constants tots els valors que poden aparéixer en una expressió. En aquest cas, però, no necessiten cap nom perquè només s’utilitzen en el lloc puntual en que apareixen.

Quan volem fer referència a variables i constants de forma conjunta, parlem d’objectes. Per tant, els objectes d’un algorisme són les seves constants i les seves variables.

Tot objecte té tres atributs:

* el nom o identificador: és el nom que li donem i que ens permet referenciar-lo.    el tipus: determina la classe de valors pot prendre: enters, reals...

* el valor: el valor que es guarda a la cel·la de memòria associada a l’objecte.

**Tipus de dades:** El tipus d’un objecte determina el conjunt de valors possibles que pot prendre, i en consequència:

* l’espai de memòria que ocupa,
* la seva representació interna,
* les operacions que es podran dur a terme amb aquell objecte.

El nostre llenguatge algorísmic reconeix quatre tipus elementals:** enter, real, carácter i boolea. Una dada de tipus **enter** pot prendre com a valor un nombre enter qualsevol: 3, 5, -34...

Una dada de tipus **real** pot prendre qualsevol valor del conjunt dels nombres reals: 2.45, 3e-5...

Una dada de tipus **caracter** pot prendre qualsevol valor d’una taula de caracters, que inclou les lletres de l’abecedari, els dígits decimals i una sèrie de símbols addicionals, com ara símbols de puntuació, espais en blanc, etc. Normalment es fa servir la taula de caràcters ASCII.

Una dada de tipus **booleà** pot prendre només dos valors: cert o fals.![](Aspose.Words.a8518bd6-be42-4fc5-a506-e71f4c9283ed.004.png)

**Tipus de dades elementals**

|**enter**|qualsevol nombre enter|512|
| - | - | - |
|**real**|qualsevol nombre real|3.5e-3|
|**caracter**|qualsevol caracter d’una taula|‘D’|
|**booleà**|només pot ser cert o fals.|cert, fals|


## Representació interna de les dades

Totes les dades a la memòria d’un computador estan codificades com una seqüència de 0’s i 1’s.

La memòria dels ordinadors està basada en l’agrupació de gran quantitat de components electrònics que poden estar en dos estats (p.ex +5V, 0V) que es representen per 0 i 1 (és a dir, un bit). Per aixó,  totes les dades emmagatzemades a la memoria d'un ordinador es codifiquen com una seqüència de bits.

**Codificació dels booleans**

Com que només hi ha dos valors possibles (cert i fals), n'hi ha prou amb un sol bit i una codificació com: fals  0  (on la fletxa “  ” la podem llegir com “...es representa amb...” ).

cert  1.

**Codificació dels enters**

Per codificar un número enter es pot ser servir la seva representació binària.

Habitualment fem servir la numeració en base 10. Aixó vol dir que en un número, el valor d'un digit (0..9) depén de la seva posició, segons una sèrie de potències de 10:



|<p>d</p><p>4</p>|<p>d</p><p>3</p>|<p>d</p><p>2</p>|<p>d</p><p>1</p>|<p>d</p><p>0</p>|
| - | - | - | - | - |
**10000 1000 100 10 1** Per exemple: 5243 = 5\*1000 + 2\*100 + 4\*10 + 3\*1

Els ordinadors fan servir una numeració en base 2, on el valor dels digits (0, 1) depén de la seva posició, peró segons una sèrie de potencies de 2:



|<p>d</p><p>8</p>|<p>d</p><p>7</p>|<p>d</p><p>6</p>|<p>d</p><p>5</p>|<p>d</p><p>4</p>|<p>d</p><p>3</p>|<p>d</p><p>2</p>|<p>d</p><p>1</p>|
| - | - | - | - | - | - | - | - |
**128 64 32 16 8 4 2 1**

Per exemple: la sequència de bits 10011 representa el número 1\*16 + 1\*2 + 1\*1 =19.

Per representar enters entre 0 i 255, n’hi ha prou amb 8 bits:

0    00000000 1    00000001 2    00000010

3    00000011 4    00000100 5    00000101

...

D’aquesta forma podem representar el valor absolut d’un enter. Per representar el signe, podem fer servir un bit addicional, o utilitzar l’anomenada notació en complement a 2, on el valor de cada posició és:

|<p>d</p><p>8</p>|<p>d</p><p>7</p>|<p>d</p><p>6</p>|<p>d</p><p>5</p>|<p>d</p><p>4</p>|<p>d</p><p>3</p>|<p>d</p><p>2</p>|<p>d</p><p>1</p>|
| - | - | - | - | - | - | - | - |
-128 64 32 16 8 4 2 1

**Codificació dels reals**

Una possible representació dels reals és la representació en coma flotant. S’obté d’aquesta manera:

* Primer agafem el número que volem representar i el normalitzem, per exemple fent que hi hagi cap un zero abans del punt decimal, i un digit significatiu (1-9) després del punt decimal:

234.56   0.23456e3. 0.023   0.23e-1

* Un cop normalitzat, l'unic que hem de fer és representar la mantissa (el que hi ha després del punt decimal) i l'exponent per separat, fent servir la codificació del enters.

Exemple: si fem servir 8 bits per la mantissa i 8 més per l’exponent:

900  0.9e3     00001001 00000011

**Codificació dels caracters**

Per codificar els caracters es fa servir una taula de traducció on cada caracter té assignat un número enter. Normalment s’utilitza un codi estandard anomenat ASCII. Per que us en feu una idea, aquí teniu el codi ASCII d’els caracters imprimibles:

: 32 !: 33 ": 34 #: 35 $: 36 %: 37 &: 38 ': 39 (: 40 ): 41 \*: 42 +: 43

,: 44 -: 45 .: 46 /: 47 0: 48 1: 49 2: 50 3: 51 4: 52 5: 53 6: 54 7: 55 8: 56 9: 57 :: 58 ;: 59 <: 60 =: 61 >: 62 ?: 63 @: 64 A: 65 B: 66 C: 67 D: 68 E: 69 F: 70 G: 71 H: 72 I: 73 J: 74 K: 75 L: 76 M: 77 N: 78 O: 79 P: 80 Q: 81 R: 82 S: 83 T: 84 U: 85 V: 86 W: 87 X: 88 Y: 89 Z: 90 [: 91 \: 92 ]: 93 ^: 94 \_: 95 : 96 a: 97 b: 98 c: 99 d:100 e:101 f:102 g:103 h:104 i:105 j:106 k:107 l:108 m:109 n:110 o:111 p:112 q:113 r:114 s:115 t:116 u:117 v:118 w:119 x:120 y:121 z:122 {:123 |:124 }:125 ~:126

Exemple:  ‘A’   65   01000001

**Unitats de memòria**

Les unitats de memòria o mesures de la quantitat d’informació són:

* **bit**: quantitat d’informació que permet distingir un valor concret d’entre 2 valors diferents.    **byte:** equival a 8 bits. Amb 8 bits es poden representar 28=256 valors diferents.
* **KB:** equival a 1024 bytes:
* **MB:** equival a 1024 KB
* **GB**: equival a 1024 MB

## Definició de constants en llenguatge algorísmic

Si volem fer servir una constant en un algorisme, cal que la definim en el bloc de definició de constants:

    algorisme Nom de l’Algorisme

    const
        {Definició de constants}
    fconst
    tipus
        {Definició de tipus} ftipus
    var
        {Declaració de variables} fvar
    {Accions}
    ...       
    falgorisme

En llenguatge algorísmic, totes les constants es defineixen en el bloc **const** i **fconst**, amb el format:

    const
    nom : tipus = valor
    fconst

Exemple (fixeu-vos que cada constant es defineix en una línia separada):

    const
    DIES\_EN\_UN\_ANY : enter = 365
    PI : real = 3.14159
    DARRERA\_LLETRA : caracter = ‘Z’ fconst

nom:

* El nom de les constants es posa normalment en majúscules.
* El nom ha de ser un identificador vàlid. Un identificador és vàlid quan:
* Només està format per lletres, números i el carácter subratllat ‘\_’, sense que puguin apareixer altres caracters com signes de puntuació o espais en blanc.
* No coincideix amb cap de les paraules clau del llenguatge (**var**, **mentre**, etc.).
* - Es tria de forma sigui expressiu del seu contingut.

tipus:

* El tipus ha de ser un dels quatre tipus elementals: **enter**, **real**, **caracter** o **boolea**. valor:
* Si la constant és un **enter**, es posa el valor de la forma habitual: 234, -12...
* Si la constant és un **real**, ha de dur o bé el punt decimal, o bé la lletra d’exponencial “e”: 12.25,

314e-2, 3.0

* Si la constant és un **caracter**, el posa entre cometes simples: ‘a’, ‘b’, ‘A’, ‘\_’, ...
Si la constant és un **boolea**, el valor només pot ser **cert** o **fals**.

## Declaració de variables en llenguatge algorísmic

Si volem fer servir una variable en un algorisme, cal que la declarem en el bloc de declaració de variables:

    algorisme Nom de l’Algorisme
        const
            {Definició de constants}
        fconst
        tipus
            {Definició de tipus} 
        ftipus
        var
            {Declaració de variables} 
        fvar
        {Accions}
        ...
    falgorisme

En llenguatge algorísmic, totes les variables es declaren en el bloc **var** i **fvar**, amb el format:

    var
        nom : tipus
    fvar

Exemple (fixeu-vos que en una mateixa línia es poden declarar més d’una variable):

    var
        dni, edat : enter 
        velocitat, temps : real 
        lletraNIF : caracter 
        es\_solter : boolea
    fvar

nom:

* El nom de les variables es posa normalment en minuscules (excepte inicials de noms compostos).    El nom ha de ser un identificador vàlid. Un identificador és vàlid quan:

- Només està format per lletres, números i el carácter subratllat ‘\_’, sense que puguin apareixer altres caracters com signes de puntuació o espais en blanc.
- No coincideix amb cap de les paraules clau del llenguatge (**var**, **mentre**, etc.).
- Es tria de forma sigui expressiu del seu contingut.

tipus:

* El tipus ha de ser un dels quatre tipus elementals: **enter**, **real**, **caracter** o **boolea**., o un tipus definit per l’usuari al bloc de definició de tipus (ho veurem més endavant).

Fixeu-vos que quan es tractava de constants parlavem de **definició** (perquè li domavem ja el valor que tindrà durant tota l’execució de l’algorisme), mentre que quan es tracta de variables parlem de **declaració** (perquè només diem com es diu la variable i de quin tipus és).  Quan una variable es declara, el seu valor resta indeterminat fins que s’hi assigna un valor inicial a una variable (inicialització).

## Operadors del llenguatge algorísmic

Amb les dades d’un determinat tipus (enter, real, caracter i boolea) podrem fer unes operacions predefinides que es corresponen amb les que sap fer la unitat aritmètico-lògica del processador. Aquestes operacions es representen amb símbols especials anomenats **operadors**.

El llenguatge algorísmic té quatre tipus d’operadors:    **Operadors aritmètics**


|**Operadors aritmètics pels enters**|
| - |
|+|Suma de dos enters, essent el resultat un enter|
|-|Resta de dos enters, essent el resultat un enter|
|\*|Producte de dos enters, essent el resultat un enter|
|**div**|Divisió entera de dos enters, essent el resultat un enter|
|**mod**|Residu de la divisió entera de dos enters, essent el resultat un enter|
Exemples:   

14 div 4  dóna com a resultat 3 14 mod 4 dóna com a resultat 2



|**Operadors aritmètics pels reals**|
| - |
|+|Suma de dos reals, essent el resultat un real|
|-|Resta de dos reals, essent el resultat un real|
|\*|Producte de dos reals, essent el resultat un real|
|**/**|Divisió de dos reals, essent el resultat un real|
Exemples: 14.0 / 4.0 = 3.5    **Operadors lògics per booleans**



|**Operadors lògics pels booleans**|
| - |
|**i**|Retorna  **cert**  quan  els  dos  operands  són  **cert**.  Als  altres  casos retorna **fals**.|
|**o**|Retorna **cert** quan qualsevol dels dos operands sigui **cert**. Quan tots dos són **fals** retorna **fals**.|
|**no**|Retorna **cert** si l’operand era **fals**, i viceversa.|
Exemple:  (a>b) i (b>c)

`   `**Operadors relacionals**

Permeten comparar dos operands del mateix tipus, segons una relació d’ordre. El resultat és un booleà.

/|**Operadors relacionals**|
| - |
|=|Igual|
|**<**|Menor|
||Menor o igual|
|**>**|Major|
||Major o igual|
||Diferent|


- L’ordre dels enters i dels reals coincideix amb l’ordre habitual.
- L’ordre dels caracters està determinat per l’ordre de la seva codificació ASCII. Fixeu-vos que en el codi ASCII es respecta l’ordre alfabètic de les lletres.
- L’ordre dels booleans (pràcticament no es fa servir) es defineix de forma arbitraria: fals < cert.

`   `**Operadors de conversió de format**

Donat que no es pot operar directament un enter amb un real, cal disposar d’operadors de conversió:



|**Operadors de conversió**|
| - |
|real(e)|Retorna  la  representació real de l’enter e.|
|enter(r)|Retorna la part entera del real r|
Exemple:

2.0 + real(3 div 4) 34 + enter(12.0 / 4.0)


**Resum de les operacions definides per cada tipus:**


|||**Operadors definits per cada tipus**|
| :- | :- | - |
||||aritmètics|lògics|relacionals|conversió|
|enter|+|-|\* div mod||=  **<   >**  |real()|
|real|+|-|\* /||=  **<   >**  |enter()|
|caracter|||||=  **<   >**  ||
|boolea||||i o no|=  **<   >**  ||
Llevat que s’indiqui el contrari, aquestes són les úniques operacions que es poden aplicar sobre les dades de tipus elementals. Qualsevol altre operació que necessitem (factorial, valor absolut, etc...) cal definir-la a partir d’aquests operadors predefinits.

**Comentaris sobre les operacions amb enters i reals**

Divisió real i divisió entera

És important diferenciar la divisió entre enters i la divisió entre reals.

La divisió entre reals és la divisió típica amb xifres decimals, que denotem amb “/”:

    5.0 /  2.0   dóna 2.5

La divisió entre enters és diferent, doncs obtenim un quocient i un residu, tots dos enters:

5 2

1 2

El quocient enter de la divisió de 5 entre 2 es denota per 5 **div** 2 El residu de la divisió de 5 entre 2 es denota per 5 **mod** 2

Conversió obligatòria entre enters i reals

És important recordar que, en una mateixa operació, no es poden barrejar directament enters amb reals (recordeu que la representació interna és diferent!).

Cal recordar també que els valors reals, per ser considerats com a tals, han de tenir o bé un punt decimal o bé la   e'' d'exponent: 1.2, 3e-3, 3.0, etc. En cas contrari es representarien internament com enters!

No és correcte fer

2.3 + 5

perquè l'operació suma requereix tots dos operands enters o tots dos reals. Si volem fer l'operació, hem de convertir un dels dos al tipus de l'altre:

enter(2.3) +5 que dóna 7, o bé:

2.3 + real(5)

que dóna 7.3 .

## ExpressionS

A  l’apartat  anterior  hem  vist  que  les  dades  (variables,  constants)  es  poden  combinar  amb  un  conjunt d’operadors predefinits. La combinació resultant s’anomena expressió:

**Expressió**: sequència de variables i constants combinades amb operadors i parèntesis. Exemples d’expressions:

    (a + 1) **mod** n
    2.0 \* PI \*512.5 ‘z’
    a > b

**Tipus d’una expressió:** El tipus d’una expressió és el tipus del resultat que s’obté quan s’avalua.

(a + 1) **mod** n és de tipus enter. 2.0 \* PI \*512.5 és de tipus real. ‘z’ és de tipus caracter. a > b és de tipus booleà!

Una expressió és correcta quan compleix tots aquests requeriments:

`   `Els operadors que conté són operadors predefinits (apartat 4.7).

`   `Tots els operadors que apareixen tenen exactament el mateix nombre d’operands que indica la seva

definició (observeu tots són binaris, excepte la negació i els de conversió, que són unaris) i el tipus d’aquests són els esperats per l’operador. Observeu que els operands poden ser variables, constats amb nom (p. ex. PI), constants sense nom (p. ex. 3.14), i altres expressions.

Exemples d’expressions incorrectes:



|**Exemples d’expressions incorrectes**|
| - |
|**Expressió**|**Raó per la qual no és vàlida**||
|a % 2|El símbol ‘%’ no correspon a cap operador del llenguatge algorísmic.||
|(a>3) no (b<2)|L’operador ‘**no’** només ha de dur té un operand, no pas dos.||
|2 + 3.0|L’operador suma ‘+’ requereix dos operands enters o dos operands reals, peró no un de cada tipus.||
|(a>3) + 4|En aquest cas, (a>3) dóna un resultat booleà, que no pot ser sumat amb un enter.||


**Definició alternativa del concepte “expressió”**

La definició constructiva que teniu a continuació ens diu com podem construir expressions vàlides.

* Un valor qualsevol, ja sigui enter, real, carácter o boolea, és considera una expressió vàlida.    Una variable és una expressió.

Una constant és una expressio.

Essent A i B expressions del mateix tipus,  un operador unari definit per A, i  un operador binari definit per A i B, llavors:

(A)  és una expressió

* A  és una expressió A   B és una expressio

**Avaluació d'expressions**

Avaluar una expressió vol dir realitzar les operacions que indica.

Ja hem vam veure la interpretació que té cada operador per separat. Ara només queda establir les regles que determinen l’ordre en que s’aparellen i s’avaluan els operadors quan una expressió conté més d’un operador.

1. Els  operadors  dels  nivells  més  interns  de  parèntesis  s’apliquen  abans  que  els  dels  nivells  més interns.
1. Dintre d’un mateix nivell de parèntesis, per  decidir l’ordre de les operacions s’utilitza una taula que determina la prioritat dels operadors, de forma que els operadors més prioritaris s’apliquen abans que els menys prioritaris:



|**Prioritat dels operadors en llenguatge algorísmic**|
| - |
|**(de més a menys prioritat)**|
|no|operador de negació|
|\* / div mod|operadors multiplicatius|
|+ -|operadors additius|
|=   **<    >**   |operadors relacionals|
|i|operador de conjunció|
|o|operador de disjunció|
3. Els operadors d’un mateix nivell de parèntesis que tinguin la mateixa prioritat s’avaluan en l’ordre en que apareixen a l’expressió, és a dir, d’esquerra a dreta.

Exemples:

    a>5 i b<4    equival a  (a>5) i (b<4)

    a + 4 > 5 o 3 + 5 mod 2 < 3  equival a  ( (a + 4) > 5 )  o  ( (3 + (5 mod 2) )<3)

Del darrer exemple es pot observar la conveniència d’utilitzar parèntesis en expressions llargues.

**Errors comuns amb expressions**

En altres àmbits es fa servir la notació

    1< a < 10

per indicar que *a* està entre 1 i 10. Observeu que en llenguatge algorísmic cal escriure-ho com:

    (1<a)  i  (a<10)

ja que la primera no és una expressió vàlida en llenguatge algorísmic.

Si *b* és una variable de tipus boolea, l’expressió

    *b* = cert

donarà  com  a  resultat  cert  quan  *b*  sigui  cert,  i  fals  quan  *b*  sigui fals.  Per  tant,  l’expressió  anterior  és equivalent a:

*b*

Anàlogament, l’expressió

*b* = fals és millor escriure-la com:
**no** b

## Accions del llenguatge algorísmic

Un cop hem definit les constants i hem declarat les variables que farem servir, cal escriure les accions que formaran el cos de l’algorisme:

    algorisme Nom de l’Algorisme

        const
            {Definició de constants}
        fconst  
        tipus
            {Definició de tipus} ftipus
        var
            {Declaració de variables} 
        fvar
        Accio1 
        Accio2 
        Accio3 
        ...
    falgorisme

El llenguatge algorísmic reconeix una acció elemental (l’assignació) i tres accions compostes o estructures de control, que es resumeixen a continuació:



|**Accions elementals i estructures de control del llenguatge algorísmic**|
| - |
|Assignació|variable := expressió|
|Estructura condicional (o alternativa)|<p>si condicio1 accio1</p><p>condicio2 accio2 ...</p><p>fsi</p>|
|Estructura iterativa “mentre”|<p>mentre condicio fer</p><p>accio</p><p>fmentre</p>|
|Estructura iterativa “per”|<p>per variable en [valor\_inicial..valor\_final] fer</p><p>accio</p><p>fper</p>|


## L’assignació

L’assignació és l’acció fonamental a partir de la qual es construeixen els algorismes. L’execució d’una assignació consisteix a avaluar una expressió i a emmagatzemar el resultat en una variable.

**Sintaxi de l’assignació en llenguatge algorísmic**

    nomVariable := expressio 

on:
* nomVariable és el nom d’una variable que haurem declarat prèviament;
* expressió és una expressió vàlida on totes les constants que conté estan definides i totes les variables que conté estan declarades i inicialitzades.

El simbol ‘:=’ s’anomena símbol de l’assignació, i es llegeix “...*pren per valor*...”.

Exemple:

    mitja := suma / n

**Validesa**

* Al costat dret deu haver una expressio vàlida (totes les variables han d'haver estat declarades i inicialitzades prèviament).
* El tipus de l'expressió i de la variable han de coincidir (enter i enter, real i real, booleà i booleà, etc.).

**Execució d’una assignació**

Una assignació s’executa en dos passos:

1. S'avalúa l'expressió del costat dret (tasca duta a terme per la unitat aritmètico-lògica)
1. El resultat s'emmagatzema dins la variable de la part esquerra. (escriptura a memòria)

Observeu que l’execució d’una assignació implica:

* una operació de lectura (consulta) per cadascuna de les variables que apareixen en l’expressió.    
* una operació d’escriptura (modificació) de la variable de la esquerra de l’assignació.

Exemple: Intercanvi de dues variables.

**Lectura de dades del canal d’entrada**

El  llenguatge  algorísmic  està  dotat  de  tres  funcions  predefinides  que  permeten  llegir  dades  del  canal d’entrada  estàndar.  Habitualment  el  canal  d’entrada  és  el  teclat,  per  tant  aquestes  funcions  permeten demanar l’entrada de dades a l’usuari (ja siguin dades enteres, reals o caracters). Aquestes tres funcions són LlegirEnter, LlegirReal i LlegirCaracter, i el seu format és:

nomVariable := LlegirEnter() nomVariable := LlegirReal() nomVariable := LlegirCaracter()

L’execució d’aquestes assignacions sobre el teclat es duu a terme així:

1. L’ordinador espera fins que l’usuari entri una dada
1. Si la dada entrada no és del tipus demanat (enter, real, caracter), es considera un error.
1. Si la dada entrada és del tipus demanat, es copia aquest valor dins la variable.

**Escriptura de dades pel canal de sortida**

El llenguatge algorísmic també està dotat de quatre accions predefinides que permeten escriure dades al canal  de sortida  estàndar  (normalment  el  canal  de  sortida  és  la  pantalla,  per  tant,  aquestes  operacions escriuen per pantalla):

**EscriureEnter**

Format:  EscriureEnter(*expressió entera*)

Resultat: Escriu pel canal de sortida el valor d’una expressió de tipus enter. Exemples: EscriureEnter(25),   EscriureEnter(a+5)

**EscriureReal**

Format:  EscriureReal(*expressió real*)

Resultat: Escriu pel canal de sortida el valor d’una expressió de tipus real Exemples: EscriureReal(25.2), EscriureReal(r/2.0)

**EscriureCaracter**

Format:  EscriureEnter(*expressió de tipus caracter*)

Resultat: Escriu pel canal de sortida el valor d’una expressió de tipus caracter.

Donat que els caracters no tenen cap operació interna, una expressió de tipus caracter només pot ser o bé un valor (ex. ‘a’), o bé el nom d’una variable de tipus caracter.

Exemples:

        const
        C : caracter = ‘Z’
        fconst

EscriureCaracter(C) {escriu per pantalla una **Z**} EscriureCaracter(‘C’)  {escriu per pantalla una **C**}

**EscriureMissatge**

Format: EscriureMissatge(“cadena de text”)

Resultat: Escriu pel canal de sortida la cadena de text delimitada per cometes dobles. Exemple: EscriureMissatge(“Entra un enter:”)

## L’estructura condicional si

L’estructura condicional permet que algunes accions s’executin només quan es compleix una determinada condició. Per tant, permet prendre decisions i seguir camins alternatius dins un algorisme.

**Sintaxi de l’estructura condicional en llenguatge algorísmic**

    si condicio 
        accio
            1 1 ...
        condicio accio
        n n
    fsi

on:

* condicio és una expressió vàlida que dóna com a resultat un booleà
* acció és qualsevol acció o conjunt d’accions vàlides (assignació o altres estructures de control).

El simbol  “  ” es pot llegir i escriure com “aleshores” o “llavors”, amb idèntic significat. 

Exemple

    si  a>b maxim:=a
        a=b maxim:=a
        a<b maxim:=b
    fsi 
    
**Execució d’una estructura condicional**

Una estructura **si** s’executa en tres passos:

1. S'avaluen totes les condicions i s’identifica quina és certa (n’hi ha d’haver exactament una).
2. S’executen les accions corresponents a la condició que ha resultat ser certa.
3. Continua l’execució de l’algorisme per la línia següent al **fsi**

**Validesa**

Perquè aquesta estructura sigui vàlida, s’han de seguir aquestes regles:

Les  condicions  condicio ,  ...  condicio ,  han  de  posar-se  de  forma  que  estiguin
contemplats tots els cassos possibles, però que no hi hagi cassos repetits. Per tant, hem de
garantir  que,  per  qualsevol  estat  possible  al  començament  del  **si,**  sempre  hi  haurà exactament una condició certa i la resta seran falses. Per aconseguir aixó, a vegades cal descomposar un **si** en més d'un nivell.

Si per algun cas del **si** no hem de fer res, posarem l'accio especial **continuar**, que no canvi l’estat de l’algorisme.

Exemple:  Càlcul del màxim de 3 numeros, etc.

## L’estructura iterativa **mentre**

L’estructura iterativa permet executar repetidament un conjunt d’accions fins que s’arribi a una determinada condició.

**Sintaxi de l’estructura iterativa en llenguatge algorísmic**

    mentre condicio fer
        accio1 
        ... 
        accion
    fmentre
on:
* condicio és una expressió vàlida que dóna com a resultat un booleà
* accio és qualsevol acció o conjunt d’accions vàlides que s’anomenen “cos del bucle”. 

Exemple

    a:=1
    mentre a<5 fer
        EscriureEnter(a) a:=a+1
    fmentre

Observeu que l’execució de l’exemple anterior escriuria per pantalla els valors 1, 2, 3 i 4. **Execució d’una estructura iterativa**

Una estructura **mentre** s’executa en tres passos:

1. S'avalua la condició de continuació.
2. Si és certa, s’executen totes les accions del cos del bucle i tornem al pas 1.
3. Si és falsa, sortim del bucle i continua l’execució de l’algorisme per la línia següent al **fmentre**

Observeu que si al comencament del bucle la condició és falsa, no s'executa el cos del bucle cap vegada. **Validesa**

Perquè aquesta estructura sigui vàlida, s’han de seguir aquestes regles:

La condicio ha de posar-se de forma que es faci falsa després d’un determinat número d’iteracions. Aixó implica que la condició ha de contenir variables, i que el valor d’almenysuna d’aquestes variables s’haurà d’alterar dins el bucle. Exemple:  Càlcul de productes, potències, factorial.

## L’estructura iterativa per

Aquesta estructura també permet executar repetidament un conjunt d’accions. De fet, és un cas particular de **mentre**, en el que sabem a priori el número d’iteracions que cal fer.

**Sintaxi de l’estructura en llenguatge algorísmic**

    per variable en [inici..fi]
        accio
            1
            ...
        accio
            n
    fper

on:
* variable és una variable declarada com enter, peró que no cal que hagi estat inicialitzada abans.
* inici i fi són enters o expressions que dónen com a resultat un enter
* accio és qualsevol acció o conjunt d’accions vàlides (assignació o altres estructures de control). Les accions dins d’un mentre s’anomenen “cos del bucle”.

Exemple

        per a en [1..4] fer
            EscriureEnter(a)
        fper

Observeu que l’execució de l’exemple anterior escriuria per pantalla els valors 1, 2, 3 i 

## Execució d’una estructura iterativa

Una estructura **per** es defineix en termes del seu equivalent amb un **mentre**:

|<p>per variable en [inici..fi]</p><p>accions</p><p>fper</p>|<p>equival</p><p>a</p>|<p>variable:=inici</p><p>mentre variable<=fi fer</p><p>accions</p><p>variable:=variable+1 fmentre</p>|
| - | - | - |

Observeu que:

* si abans del **per** es cumpleix que inici=fi, llavors el cos del bucle només s’executa una vegada (només es fa una iteració).
* si abans del **per** es cumpleix que inici>fi, llavors el cos del bucle no s’executa cap vegada. Exemple:  Càlcul de productes, potències, factorial.

