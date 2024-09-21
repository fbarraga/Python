
# Exercicis de Tipus de Dades Simples

1. Escriure un programa que mostri per pantalla la cadena !Hola Mundo!.

2. Escriure un programa que emmagatzemi la cadena !Hola Mundo! en una variable i després la mostri per pantalla el contingut de la variable.

3. Escriure un programa que mostri per pantalla el resultat de la següent operació aritmètica 3+2

4. El següent codi imprimeix un missatge amb un nom i una edat, però aquests valors estan escrits directament dins el codi. Modifica el codi per utilitzar variables per al nom i l’edat. Per a fer-ho:<br>
     1. Crea una variable nom per guardar el nom "Anna". <br>
     2. Crea una variable edat per guardar l’edat 25.<br>
     3. Substitueix els valors fixos per les variables en les instruccions print.
```text
print("El meu nom és Anna.") 
print("Tinc 25 anys.")
```
     
5. Escriu un programa que calculi el preu final d'un producte, incloent-hi l'impost. Utilitza variables per representar el preu base i el percentatge d'impost. Per a fer-ho:<br>
     1. Declara una variable preu_base i assigna-li el valor 100.<br>
     2. Declara una variable impost i assigna-li el valor 0.21 (21% d’impost).<br>
     3. Calcula el preu final guardant el resultat en una nova variable anomenada preu_final.<br>
     4. Mostra el preu final amb un missatge descriptiu.

6. El següent codi mostra el preu d’un producte, però ara volem aplicar-hi un descompte. Modifica el codi per calcular el nou preu amb un descompte del 10%. Per a fer-ho: <br>
     1. Crea una variable descompte i assigna-li el valor 0.10 (10% de descompte).
     2. Modifica la variable preu per aplicar-hi el descompte.
     3. Mostra el nou preu amb un missatge descriptiu.
```text
preu = 50
print(f"El preu original és {preu} euros.")
```

7. Escriure un  un programa que pregunti el nom de l'usuari a la consola i després de que l'usuari l'introdueixi mostri per pantalla la cadena ¡Hola <nom>!, on <nom> és el nom que l'usuari hagi introduit.

8. Escriure un programa que pregunti a l'usuari pel número d'hores treballades i el cost per hora. Després haurà de mostrar per pantalla la paga que li correspon.

9. Escriure un programa que llegeixi un enter positiu, n, introduit per l'usuari i després mostri per pantalla la suma de tots els enters des d'1 fins a n.

10. Escriure un programa que demani a l'usuari el seu pes (en kg) i alçada (en metres), i calculi l'índex de massa corporal i ho guardi en una variable. Després  ha de mostrar per pantalla la frase "El teu índex de massa corporal és <imc>"  on <imc> es la variable on heu guardat el càlcul arrodonit a dos decimals.

     ```text
    Després de calcular-ho en funció del valor que surti que et digui en quin segment estàs.
    Peso bajo = menos de 18.5;
    Peso normal = 18.5 a 24.9;
    Sobrepeso = 25 a 29.9;
    Obesidad = 30 a 35;
    Obesidad mórbida = 35 y más.
     ```

11. Escriure un programa que demani a l'usuari dos nombres enters (n,m) i mostri per pantalla  el quocient (c) i el residu (r) com a resultat de dividir n per m.

12. Escriure un programa que pregunti a l'usuari una quantitat a invertir, l'interés anual i el número d'anys, i mostri per pantalla el capital obtingut en la inversió.

13. Una botiga de joguines té molt èxit en dos dels seus productes: pallassos i nines. Sol fer la venda per correu i l'empresa de logística cobra pel pes de cada paquet. Per tant, han de calcular el pes dels pallassos i de les nines que sortiran en cada paquet que es demani. Cada pallasso pesa 112g i cada nina 75g. Escriure un programa que llegeixi el número de pallassos i nines venudes en la darrera comanda i calculi el pes total del paquet que serà enviat.

14. Imagina que acabes d'obrir un nou compte d'estalvi que t'ofereix el 4% d'interés anual. Aquests interessos no es cobren fins a final d'any, quan s'afegeixen al balanç final del teu compte. Esciure un programa que comenci llegint la quantitat de diners depositada al compte d'estalvis. Després ha de calcular i mostrar per pantalla la quantitat d'estalvis després del primer, segon i tercer any. Arrodonir cada quantitat a dos decimals.

15. Una fleca ven barres de pa a 3.49€ cada una. El pa que no és del día té un descompte del 60%. Escriure un programa que comenci llegint el número de barres que tenim d'avui i d'ahir. A partir d'aquí haurà de demanar les barres que venem i el programa haurà de mostrar el preu total de les barres de pa considerant els diferents preus segons el tipus.

16. Definir una funció max() que agafi com argument dos números i retorni el més gran dels dos.. (Python té una función max() incorporada, pero hem de fer una nosaltres mateixos).

17. Definir una funció max_de_tres(), que agafi tres números com arguments i retorni el més gran d' ells.

18. Definir una funció que calcule la longitud d'una llista o una cadena donada. (Amb python hi ha la función len() , però hem d'escriure la nostra des de zero).

19. Escriure una funció que demani un caràcter i retorni True si és una vocal, en cas contrari retorna False.

20. Escriure una funció sum() i una funció multip() que sumin i multipliquin respectivament tots els números d'una llista. Per eexemple: sum([1,2,3,4]) hauria de retornar 10 i multip([1,2,3,4]) hauria de retornar 24.

21. Definir una funció inversa() que calculi la inversa d'una cadena. Per exemple la cadena "estoy probando" hauria de retornar la cadena "odnaborp yotse"

22. Definir una funció es_palindromo() que reconeix els palíndroms (és a dir, paraules que tenen el mateix aspecte quan les escrius al revés), exemple: es_palindromo ("radar") hauria de retornar True.

23. Definir una funció superposicio() que agafi dues llistes i retorni True si tenen al mennys 1 membre en comú o retorni False de lo contrari. Escriure la funció utilitzant el bucle for aniuat.

24. Definir una funció generar_n_caracters() que prengui un enter n i retorna el caràcter multiplicat por n. Per exemple: generar_n_caracters(5, "x") hauria de retornar "xxxxx".

25. Definir un histograma procediment() que agafi una llista de números enters i imprimeixi un histograma a la pantalla. Exemple: procediment([4, 9, 7]) hauria d'imprimir:

    ```text
    ****
    *********
    *******
    ```

26. La funció max() i la funció max_de_tres() fets anteriorment, només funcionen per 2 o 3 números. Suposem que tenim més de 3 números o no sabem quants números ens entraran. Escriure una funció max_in_list() que agafi una llista de números i retorni el més gran.

27. Escriure una funció mes_llarga() que agafi una llista de paraules i retorni la més llarga.

28. Escriure una funció filtrar_paraules() que agafi una llista de paraules i un enter n, i retorni les parauless que tinguin més de n caràcters.

29. Escriure un programa que demani a l'usuari que ingresi una cadena. El programa ha d'avaluar la cadena i dir quantes lletres minúscules té.

30. Construir un programa que converteixi números binaris en enters (no facis servir les built-in de python).

31. Escriure un programa on:

    - Es demani l'any en curs.
    - Es demani el nom i l'any de naixement de tres persones.
    - Es calcula quants anys cumplirán durant l'any en curs.
    - S'imprimeix per pantalla.

32. Demanar a l'usuari que entri 10 edats de persones i desa-ho en una tupla.
Imprimir la quantitat de persones amb edats superiors a 20.

33. Definir una llista amb un conjunt de noms, imprimir la quantitat que comencen amb la lletra a.
També es pot fer escollir a l'usuari la lletra a buscar. 

34. Crear una funció comptar_vocals(), que rebi una paraula i compti quantes lletres "a" té, quantes lletres "e" té i així fins completar totes les vocals

35. Escriu una función es_traspas() que determini si un any determinat és un any de traspàs(), és a dir, és divisible per 4, però no per 100, excepte que sí que és divisible por 400.
