# Bots de Telegram

Basat en Lliçons Jordi Petit UPC https://xn--llions-yua.jutge.org/python/telegram.html
Actualitzat per Francesc Barragan amb noves llibreries de Telegram-BOT v20.2  llibreries a Maig 2023


Telegram és una aplicació de missatgeria instantània gratuïta i feta amb programari lliure que permet enviar i rebre missatges a través d’Internet. Un dels seus objectius és proveir una major privadesa i seguretat en comparació amb altres aplicacions similars. Telegram permet crear grups, enviar imatges o vídeos i programar bots (robots) que atenen peticions dels usuaris.

Aquesta lliçó explica com escriure un bot de Telegram utilitzant Python. Inclou exemples per fer bots amb traducció de llengües, tickers de borsa i mapes, entre d’altres.

## Requeriments

1. Primer us heu d’instal·lar i configurar Telegram al vostre telèfon mòbil.
Nota: Si sou menors, consulteu la Guia de menors a Internet i demaneu permís als vostres pares o tutors legals.

2. També us serà útil instal·lar Telegram al vostre ordinador, per no haver d’anar provant les coses al telèfon.

3. A l’ordinador on s’executarà el vostre bot, heu d’instal·lar la llibreria python-telegram-bot. Aquests exercicis estan provats amb la darrera versió de la llibreria (20.2). Per instal·lar-jo heu de fer:

```python
pip3 install python-telegram-bot
(O pip segons el vostre sistema.)
```

4. Necessiteu un Access token, que és un identificador que Telegram us dóna per identificar el vostre bot. Aquest pas només cal que el feu un cop per bot. Essencialment:

   * Visiteu el @BotFather des de l'aplicació de Telegram.
   * Useu la comanda /newbot i doneu la informació que us demana (nom complet i nom d’usari del bot, que ha d’acabar amb bot).
   * Deseu en un fitxer token.txt el vostre access token, que té un aspecte com ara xxxxxxxxxxxxxxxxxx.
   * Apunteu l’adreça del vostre bot, que té un aspecte com ara <https://t.me/CampalansBot>.

![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/telegram_campalanet.png?raw=true)

**Nota**: L’access token no l’heu de compartir, altrament, algú altre podria substituir el vostre bot. Aneu amb en compte de no desar-lo en un repositori de GitHub, per exemple.

Les instruccions completes les podeu trobar a <https://core.telegram.org/bots#6-botfather>.

## Provant un primer bot (Hello bot)

Escriviu aquest programa en un fitxer [bot1.py](./bot1.py):

```python
# importa l'API de Telegram
from telegram.ext import Application, CommandHandler,ContextTypes
from telegram import Update

# defineix una funció start que saluda i que s'executarà quan el bot rebi el missatge /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Inform user about what this bot can do"""
    await update.message.reply_text(
        "👏👏 Felicitats! Tot el món mundial ja pot parlar amb el bot del Campalans!!! 🎉 🎊"

    )

def main():
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('./token.txt').read().strip()
    print(TOKEN)
    
    application = Application.builder().token(TOKEN).build()
    #Definim les opcions que podrà executar
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
```

Executeu-lo amb

```python
python3 bot1.py
```

i amb un navegador, visiteu l’adreça del vostre bot que us ha donat el @BotFather. Això us redirigirà al Telegram i entrareu en una conversa amb el vostre bot. Doneu-li la comanda /start (o piqueu el botó Inicia’l) i ell us contestarà:

👏👏 Felicitats! Tot el món mundial ja pot parlar amb el bot del Campalans!!! 🎉 🎊

Nota: Sempre va una mica lent a engegar-se.

Si no funciona, comproveu el vostre access token o mireu si ha canviat alguna cosa a la llibreria de Telegram. Moltes vegades amb les noves versions hi ha canvis en les crides o mètodes.

Podeu aturar el vostre bot interrompent el vostre programa (amb Control+C). Llavors els usuaris ja no hi podran interactuar fins que no el torneu a encendre.

# Explicació del primer bot

El bot s’executa en el vostre ordinador. Els usuaris es connecten a ell a través de Telegram, que fa d’intermediari. El vostre bot utilitza l’API de [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) per realitzar totes les comunicacions necessàries.

El programa anterior fa que quan el bot rebi la comanda /start, contesti amb el missatge "Felicitats...."

Per a fer-ho, primerament, el programa importa algunes funcions de l’API de Telegram:

```python
from telegram.ext import Application, CommandHandler,ContextTypes
from telegram import Update
```

Després, el programa defineix la funció start.

A continuació, el programa crea un sèrie d’objectes necessaris per establir la comunicació i el control de flux. Per a fer-ho, necessita el vostre access token, que llegeix del fitxer token.txt:

```python
def main():
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('./token.txt').read().strip()
    print(TOKEN)
    
    application = Application.builder().token(TOKEN).build()
```

Amb això, ara vincula la funció start amb la comanda /start, utilitzant les crides

```python
application.add_handler(CommandHandler('start', start))
```

Finalment, el bot es posa en marxa amb aquestes comandes:

```python
application.run_polling()
```

Per la seva part, la funció start és aquesta:

```python
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Inform user about what this bot can do"""
    await update.message.reply_text(
        "👏👏 Felicitats! Tot el món mundial ja pot parlar amb el bot del Campalans!!! 🎉 🎊"
    )
```

Aquesta funció s’executarà cada cop que un usuari escrigui la comanda /start, perquè així ho hem dit amb el add_handler. Els seus paràmetres update i context són objectes que ens permeten tenir més detalls de la informació de l’usuari i realitzar accions amb el bot. En aquets cas, el bot senzillament envia un missatge amb el text donat.

Tot bot ha de tenir una comanda /start.

## Un primer exercici

Anem a modificar el programa anterior per tal de reconèixer dues comandes més: /help que ha de donar informació sobre el vostre bot i /hora, que ha de retornar l’hora actual. Així:

Teniu la solució completa a [bot2.py](./bot2.py). Fixeu-vos com Telegram entén les comandes /start i /help.

## Missatges multimèdia

Els missatges de resposta poden ser més rics que un trist missatge de text (que pot incloure emojis):

* Per enviar missatges formatejats en *Markdown*, cal usar el mètode send_message tot indicant `parse_mode=telegram.ParseMode.MARKDOWN`. Per enviar missatges formatejats en HTML, cal usar el mètode send_message tot indicant `parse_mode=telegram.ParseMode.HTML`. 

* Per enviar missatges amb imatges, cal usar el mètode `send_photo` tot indicant la URL de la imatge amb photo=URL. Si enlloc d’una URL es passa un fitxer local obert amb open, s’enviarà aquell fitxer (comproveu que existeixi per provar-ho!). També hi ha formes semblants d’enviar audio o vídeo.

La funció start següent ho demostra amb alguns exemples:

```python
def start(update, context):
    info = '''
```

Aquí es pot escriure en MarkDown:

* En *negreta*
* En *cursiva*

```python
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://github.com/fbarraga/Python/blob/master/master/assets/telegram_campalanet.png')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('imatge.png', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text=" 🎗️ ")
```

Assegureu-vos de tenir un fitxer `imatge.png` al mateix directori perquè l’open el pugui llegir.

## Altres opcions

Al nostre bot també podem demanar-li que faci altres opcions per defecte, com per exemple enquestes:

```python 
async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a predefined poll"""
    questions = ["Muy Malo", "Malo", "Bueno", "Muy Bueno"]
    message = await context.bot.send_poll(
        update.effective_chat.id,
        "Que tipo de estudiante eres?",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )
```

Pots consultar el codi en el [bot3.py](./bot3.py).


## Informació del bot i de la conversa

Com s’ha dit, els objectes bot i update que reben les funcions per tractar comandes contenen informació sobre el bot i la conversa. En particular:

* update.message.text conté el text enviat per l’usuari,
* context.bot.username conté el nom del nostre bot,
* update.effective_chat.username,
* update.effective_chat.first_name i
* update.effective_chat.last_name contenen dades de l’usuari amb qui es manté la conversa.

La funció start següent demostra aquestes facilitats:

```python
async def start(update, context):
    print(update)
    print(context)
    botname = await context.bot.username
    username = update.effective_chat.username
    fullname = update.effective_chat.first_name + ' ' + update.effective_chat.last_name
    missatge = "Tu ets en %s (%s) i jo soc el %s." % (fullname, username, botname)
    message = await context.bot.send_message(chat_id=update.effective_chat.id, text=missatge)
```

Fixeu-vos que aquesta funció també escriu els valors d’update i de context. Volcar-ne el contingut és la manera més senzilla de saber què contenen!

## Un bot traductor

Considereu que volem dotar el nostre bot d’una comanda /trad per traduir textos a l’anglès. Per exemple:

Per a fer-ho, instal·leu el mòdul `googletrans` amb

```python
pip3 install googletrans
```

Usar-lo és ben fàcil:

```python
>>> from googletrans import Translator
>>> translator = Translator()
>>> translator.translate('quan les oques van al camp, la primera va al davant').text
'When the geese go to the field, the first one goes ahead'
```

I per integrar-lo al nostre bot, caldria vincular una funció trad a la comanda /trad:

```python
dispatcher.add_handler(CommandHandler('trad', trad))
```

amb aquesta implementació:

```python
async def trad(update, context):
    miss_orig = update.message.text[6:]  # esborra el "/trad " del començament del missatge
    miss_trad = translator.translate(miss_orig).text
    message= await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=miss_trad)
```

Teniu el programa complet a [bot-trad.py](./bot_trad.py).

## Arguments a les comandes

Com s’ha dit abans, el missatge complet enviat per l’usuari es pot obtenir consultant update.message.text. Tantmateix, sovint és més fàcil usar comandes amb arguments:

Les comandes que s’envien al bot poden tenir arguments que reben a la funció que s’encarrega del seu tractament a la llista context.args. Per exemple, si volem fer una comanda /suma que calculi la suma de dos nombres donats (amb una comanda com ara /suma 21 3.5), podríem definir aquesta funció:

```python
async def suma(update, context):
    try:
        x = float(context.args[0])
        y = float(context.args[1])
        s = x + y
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(s))
    except Exception as e:
        print(e)
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')
```

Fixeu-vos que la funció suma utilitza un bloc try-except. Si es produeix qualsevol error (excepció) dins del try, es salta al except. En aquest cas, s’escriu l’error pel terminal amb el print, i s’envia un missatge d’error a l’usuari. Si no hi ha cap error, no s’executa el except.

*Exercici*: Afegiu una comanda /fibo que calculi el nombre de Fibonacci de l’argument donat. Per exemple, el bot ha de contestar 6765 per a la comanda /fibo 20. Controleu els errors.

# Mantenir l’estat de la conversa amb un usuari

En algunes situacions, es vol mantenir informació sobre l’estat d’una conversa amb un usuari entre dues comandes. Per a fer-ho, s’utilitza context.user_data, que és un diccionari per desar informacions per l’usuari amb qui ens estem comunicant (aquest diccionari és diferent per a cada usuari amb qui el bot estigui comunicant-se).

Per exemple, suposem que cada vegada que l’usuari envïi una comanda /counter, volguem incrementar un comptador que comenci a zero i retornar-lo com a resposta. Ho podríem implementar així:

```python
async def counter(update, context):
    if 'counter' not in user_data:
        context.user_data['counter'] = 0
    message = await context.user_data['counter'] += 1
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(context.user_data['counter']))
```

Proveu l’aplicació amb un parell d’usuaris diferents. Veureu que cadascun té un comptador independent de l’altre.

Fixeu-vos que aquests objectes només viuen a la memòria mentre el procés s’executa. Un cop s’aturi i es torni a engegar, es perdran. Si això no és desitjable, cal recórrer a desar-los en fitxers o en una base de dades.

# Obtenció de la localització

Si l’usuari decideix enviar al bot la seva posició (clicant l’opció Localització 📌 que surt al clicar el clip), el bot reb una petició especial que es pot vincular a una funció per tractar-la així:

```python
application.add_handler(MessageHandler(Filters.location, where))
```

La funció de tractament vinculada (where, en aquest exemple) reb un update amb la latitud i la longitud de la posició de l’usuari:

```python
async def where1(update, context):
    lat, lon = update.message.location.latitude, update.message.location.longitude
    print(lat, lon)
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Ets a les coordenades %f %f' % (lat, lon))
```

Ara podem ampliar la funció where perquè torni com a resposta un mapa centrat a la posició de l’usuari. Per a fer-ho, usarem el mòdul staticmap descrit a Fitxers i formats en Python:

```python
async def where2(update, context):
    try:
        lat, lon = update.message.location.latitude, update.message.location.longitude
        print(lat, lon)
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        mapa = StaticMap(500, 500)
        mapa.add_marker(CircleMarker((lon, lat), 'blue', 10))
        imatge = mapa.render()
        imatge.save(fitxer)
        message = await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(fitxer, 'rb'))
        os.remove(fitxer)
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')
```

Teniu el programa complet a bot-mapa.py. I aquest és un exemple d’ús del bot:

## Obtenció de la localització en directe

Les darreres versions de Telegram també permeten compartir la localització en directe: Durant un cert marge de temps, el client va informant al servidor de les noves coordenades de l’usuari. Per alguna raó estranya, per obtenir la localització en directe cal fer un codi una mica estrany:

```python
def where(update, context):
    '''aquesta funció es crida cada cop que arriba una nova localització d'un usuari'''

    # aquí, els missatges són rars: el primer és de debò, els següents són edicions
    message = update.edited_message if update.edited_message else update.message
    # extreu la localització del missatge
    lat, lon = message.location.latitude, message.location.longitude
    # escriu la localització al servidor
    print(lat, lon)
    # envia la localització al xat del client
    context.bot.send_message(chat_id=message.chat_id, text=str((lat, lon)))
```

## Informació addicional

Amb això ja teniu les bases necessàries per fer bots en Telegram. Evidentment, es poden fer moltes més coses, incloent jocs i transaccions comercials. Podeu trobar una informació més exhaustiva en aquests enllaços:

<https://core.telegram.org/bots>

<https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API>

<https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot>

