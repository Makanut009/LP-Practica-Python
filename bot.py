import sys
import traceback

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from Skyline import Skyline
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

import pickle
import matplotlib.pyplot as plt


def start(update, context):
    text = "Benvingut a SkyLineBot!\n" \
        + "Usa /help per veure les comandes disponibles."
    sortida(update, context, text)


def help(update, context):
    text = "Sóc un bot amb les següents comandes:\n" \
        + "/start: inicia la conversa amb el Bot\n" \
        + "/author: escriu el nom i correu de l'autor\n" \
        + "/lst: mostra els identificadors definits i " \
        + "la seva corresponent àrea\n" \
        + "/clean: esborra tots els identificadors definits\n" \
        + "/save id: guarda un skyline amb el nom id.sky\n" \
        + "/load id: carrega un skyline de l’arxiu id.sky"
    sortida(update, context, text)


def author(update, context):
    text = "SkylineBot (@SkyLine4Bot)\n" \
        + "Autor: Jordi Cluet Martinell\n" \
        + "Correu: jordi.cluet@upc.edu"
    sortida(update, context, text)


def lst(update, context):

    skys = context.user_data['visitor'].taula_simbols \
        if 'visitor' in context.user_data else {}

    if not skys:
        text = "No hi ha cap identificador definit"
    else:
        text = "id -> àrea"
        for id, sky in skys.items():
            text += "\n" + id + " -> " + str(sky.area())

    sortida(update, context, text)


def clean(update, context):
    if 'visitor' in context.user_data:
        context.user_data['visitor'].taula_simbols = {}
    text = "Identificadors eliminats"
    sortida(update, context, text)


def sortida(update, context, text):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def load(update, context):
    id = ' '.join(context.args)
    nom = id + ".sky"

    try:
        sky = llegeix_pickle(nom)
        if 'visitor' not in context.user_data:
            context.user_data['visitor'] = EvalVisitor()
        context.user_data['visitor'].taula_simbols[id] = sky
        text = "Skyline " + id + " carregat"

    except FileNotFoundError:
        text = "El fitxer " + nom + " no existeix"

    except Exception:
        text = "Error en carregar l'Skyline. Comprova la terminal"

    sortida(update, context, text)


def save(update, context):
    id = ' '.join(context.args)

    simbols = {}
    if 'visitor' in context.user_data:
        simbols = context.user_data['visitor'].taula_simbols
        if id in simbols:
            sky = simbols[id]
            nom = id + ".sky"
            escriu_pickle(sky, nom)
            text = "Skyline guardat com a " + nom
            sortida(update, context, text)
            return

    text = "Aquest identificador no existeix"
    sortida(update, context, text)


def llegeix_pickle(fitxer: str):
    """Llegeix un objecte d'un fitxer pickle."""
    with open(fitxer, "rb") as file:
        return pickle.load(file)


def escriu_pickle(obj: object, fitxer: str):
    """Guarda un objecte en un fitxer pickle."""
    with open(fitxer, "wb") as file:
        return pickle.dump(obj, file)


def genera_grafic(sk: Skyline):
    xs = []
    hs = []
    ws = []
    e1 = sk.edificis[0]
    for i in range(1, len(sk.edificis)):
        e2 = sk.edificis[i]
        if e1[1] > 0:
            xs.append(e1[0])
            hs.append(e1[1])
            ws.append(e2[0] - e1[0])
        e1 = e2

    plt.bar(xs, hs, width=ws, align='edge', color=['red'])
    plt.savefig('plot.png')
    plt.close()


class MyErrorListener(ErrorListener):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self):
        raise Exception

    def reportAmbiguity(self):
        raise Exception

    def reportAttemptingFullContext(self):
        raise Exception

    def reportContextSensitivity(self):
        raise Exception


def entrada(update, context):

    input_stream = InputStream(update.message.text)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    parser.addErrorListener(MyErrorListener())

    tree = None

    try:
        tree = parser.root()
    except Exception as err:
        text = "Error en parsejar l'expressió. Comprova la terminal."
        sortida(update, context, text)
        raise

    try:
        if 'visitor' not in context.user_data:
            context.user_data['visitor'] = EvalVisitor()
        (var, sk) = context.user_data['visitor'].visit(tree)
        genera_grafic(sk)

        context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open('plot.png', 'rb')
        )
        sortida(update, context, "area: " + str(sk.area()))
        sortida(update, context, "alçada: " + str(sk.alcada()))

        # print("Var: ", var)
        # print("Nombre d'edificis: ", len(sk.edificis))
        # print("Edificis: ", sk.edificis)

    except KeyError:
        text = "Aquest identificador no existeix."
    except TypeError:
        text = "Error de tipus: operació no suportada."
    except Exception as err:
        text = "Hi ha hagut una excepció. Comprova la terminal."
        print(traceback.format_exc())
        print(sys.exc_info())

    sortida(update, context, text)


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()
# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi una comanda s'executi la funció corresponent
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('save', save))

updater.dispatcher.add_handler(MessageHandler(Filters.text, entrada))

# engega el bot
updater.start_polling()
