# Crawling, Scraping i Parsing 

El web scraping (“raspat” de pàgines web) consisteix en l'extracció de les dades significatives d'una o varies pàgines web determinades, per una manipulació o anàlisi posterior.
Els conceptes de web crawling o web spider, es refereixen concretament a que per obtenir les pàgines web que ens interesen hem de rastrejar els seus enllaços web, realizant una exploració recursiva de tots els seus enllaços. Normalment, s'ha de parsejar les dades per extreure les parts que ens interesen.

## Web scraping i crawling

Les tècniques de web scraping i crawling permeten extreure dades web i analizar-les, amb moltes possibilitats finals com ara: 
    * Alimentar una base de dades 
    * Fer una migració d'un website 
    * Recopilar i oferir dades disperses per varies webs 
    * Generar alertes 
    * Monitorizació de preus de la competència 
    * Localizació d'ítems o stock en eCommerces 
    * Recolecció de fitxes de productes 
    * Detecció de canvis en websites 
    * Registrar llançaments i novetats 
    * Analitzar els enllaços d'un website per buscar links trencats 
    * ...

## Aranyes web o crawlers

Una aranya web és un programa que inspecciona les pàgines del World Wide Web de forma metòdica i automatitzada. El seu ús més freqüent es centra en: 

    * Crear una copia de totes les pàgines web visitades 
    * Processat posterior per un motor de búsqueda que indexa les pàgines. 
    * Sistema de cerques ràpid. 
  
Las aranyes web solen ser bots.

Funcionament:

1. Les aranyes visiten una llista de URLs. 
2. Es descarreguen les pàgines. 
3. Identifica els hiperenllaços. 
4. Els afegeix a la llista a visitar recurrentement. 
5. Després descarrega aquestes pàgines noves. 
6. Analitza els seus enllaços. 
7. i repeteix...


![webcrawler](https://github.com/fbarraga/Python/blob/master/master/assets/crawler.png?raw=true)


## Problemes al extreure dades web 

Existeix certa controversia sobre el scraping i algunes webs. Quant més interessants siguin les dades proporcionades per una web, intentarán protegir-los i evitar les tècniques de web scraping o crawling. 

Els accesos a una web que no es corresponen amb “accions humanes” (per ejemplo, el número de pàgines solicitades per minut), pot provocar el bloqueig de la IP.

Es convenient mirar atentament els termes legals de la web i tener en consideració els aspectos legals per la utilizació de les dades obtingudes mitjançant web scraping.

Per exemple: http://www.facebook.com/terms.php ens recorda que està prohibit l'ús de scripts automatitzats.



