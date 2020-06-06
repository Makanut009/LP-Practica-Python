# SkylineBot - Pràctica de Python

Documentació de la Pràctica de Python de l'assignatura de Llenguatges de Programació. 
Facultat d'Informàtica de Barcelona, UPC. Juny de 2020.

## Prerequisits

Perquè el bot funcioni cal tenir instal·lats els paquets que es detallen al fitxer ```requirements.txt```. Són els bàsics
mencionats a l'enunciat, i es poden instal·lar mitjançant pip3:
```bash
$ pip3 install -r requirements.txt
```
A més, cal tenir instal·lat Telegram en algun dispositiu.

## Execució

Per córrer el bot cal executar ```python3 bot.py``` des del directori arrel.
Un cop fet això, tan sols cal enviar missatges al bot (usuari @SkyLine4Bot) mitjançant Telegram, seguint les pautes que es detallen a l'enunciat.

## Detalls de la implementació

### Bot

El detalls més destacables de la implementació del bot són els següents:
 - Manté una sessió (taula de símbols) diferent per a cada usuari, que es passa com a paràmetre al visitor i que
   s'actualitza quan hi ha una assignació, es carrega un nou skyline o es buida la llista explícitament.
 - Controla els errors durant el parsejat: he implementat una classe senzilla que hereda d'```ErrorListener```
   i creat una nova excepció per tal de detectar quan es produeixen errors durant el parsejat de l'expressió.
   Sinó, és difícil saber què ha provocat l'error.
 - Quan es genera la figura d'un skyline, es guarda temporalment en un fitxer tmp.png, que s'elimina un cop
   enviat al xat de Telegram.


### Classe Skyline

Els detalls de la implementació de la classe Skyline més rellevants són els següents:

#### Creació de l'skyline

Hi ha tres maneres de crear un skyline: la creació simple ```(xmin,h,xmax)```, la creació composta ```[(xmin, alçada, xmax), ...]```,
i la creació aleatòria ```{n, h, w, xmin, xmax}```.

Tant per la creació composta com per la creació aleatòria uneixo tots els edificis recursivament. La funció ```unio_rec```
va dividint la llista en 2 i unint els skylines resultants de la unió de les subllistes de manera recursiva, fent ús de
la funció ```unio```. Fer-ho d'aquesta manera permet que les unions es produeixin entre skylines de mida similar (i la
funció unió que he implementat es comporta millor en aquests casos que quan es skylines tenen mides molt diferents) i que
es minimitzi considerablement el nombre d'unions per cada edifici i, en conseqüència, la complexitat de la operació.
Això es nota molt per a la creació aleatòria, ja que fer la unió recursiva permet tenir temps inferiors a 2 segons per a
la creació d'un skyline prou gran com aquest: ```{100000,20,3,1,10000}```.

Per a la creació aleatòria, a més, s'usa un generador aleatori d'edificis, que genera `n` edificis seguint les restriccions
de l'enunciat, per després unir-los recursivament tal i com s'ha explicat.

#### Unió i intersecció

Per minimitzar la complexitat d'aquestes dues operacions (i especialment per garantir l'eficiència en les unions
durant la creació composta o aleatòria d'skylines), defineixo un iterador per cada skyline que s'ha d'unir o intersecar,
per poder anar avançant paral·lelament pels dos skylines. A cada iteració es comparen els dos edificis apuntats pels dos
iteradors, i s'afegeix un edifici o altre a la llista final segons els diferents casos.

Com que a cada iteració s'incrementa un dels dos (o ambdós) iteradors, podem assegurar que només recorrerem els edificis 
de cada skyline una vegada i que, per tant, farem com a molt `n` + `m` comparacions, on `n` i `m` són el nombre d'edificis de
cada skyline respectivament. 

A més, he afegit algunes línies per evitar fer massa càlculs innecessaris en alguns casos, com ara quan dos skylines no
intersequen en cap punt (això es pot comprovar amb dos accessos constants, i es pot retornar directament l'skyline
buit) o quan ja hem recorregut un dels dos skylines a unir (aleshores podem afegir tota la resta d'edificis de l'altre
skyline directament, sense fer comparacions).

#### Altres operacions

Per a les altres operacions entre skylines (replicació, desplaçaments i negació) també he intentat minimitzar-ne al màxim
la complexitat. He fet ús d'elements molt útils del llenguatge, com ara funcions anònimes, funcions d'ordre superior, i
llistes per comprensió. Per exemple, en el cas de la negació (mirall) d'skylines, he usat la funció reverseD(), que retorna
un iterador que recorre la llista en sentit invers, ja que és més eficient que crear la llista recorrent-la en sentit
normal i després girar-la amb reverse().


#### Gramàtica i visitor

La gramàtica segueix l'estructura que es pot intuïr de l'enunciat:
 - el missatge (root) és o bé una assignació, o bé una expressió
 - una assignació és de la forma ```variable/identificador := expressió```
 - una expressió és, o bé un símbol (número o variable/identificador), o bé algun tipus d'skyline (senzill, compost o
   aleatori), o bé una expressió entre parèntesi, o bé una operació entre expressions.

He procurat que es compleixi l'ordre de prioritat entre operacions que marca l'enunciat.

El visitor senzillament recorre l'arbre generat seguint l'estructura explicada, i retorna una parella
(identificador, skyline), on l'identificador es correspon a la variable en cas d'una assignació i és None 
en cas que només sigui una expressió. L'skyline retornat és el resultant d'avaluar l'expressió. 
En inicialitzar el visitor, el bot li passa com a paràmetre la taula de símbols de l'usuari, per poder
accedir als valors dels identificadors ja definits.


## Construït amb

* [ANTLR4](https://www.antlr.org/) - Eina per al reconeixement de llenguatge
* [python-telegram-bot](https://python-telegram-bot.org/) - Interfície per a l'API de bots de telegram per python
* [matplotlib](https://matplotlib.org/) - Eina per generar gràfics


## Autor

* **Jordi Cluet Martinell**
