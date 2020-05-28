import sys
import os
import traceback
import pickle
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

from Skyline import Skyline

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    """Dona la benvinguda al bot."""
    text = "Benvingut a SkyLineBot!\n" \
        + "Usa /help per veure les comandes disponibles."
    sortida(update, context, text)


def help(update, context):
    """Llista les comandes disponibles."""
    text = "Sóc un bot amb les següents comandes:\n" \
        + "/start: inicia la conversa amb el Bot\n" \
        + "/help: llista les comandes disponibles\n" \
        + "/author: escriu el nom i correu de l'autor\n" \
        + "/lst: mostra els identificadors definits i " \
        + "la seva corresponent àrea\n" \
        + "/clean: esborra tots els identificadors definits\n" \
        + "/save id: guarda un skyline amb el nom id.sky\n" \
        + "/load id: carrega un skyline de l’arxiu id.sky"
    sortida(update, context, text)


def author(update, context):
    """Escriu el nom i correu de l'autor."""
    text = "SkylineBot (@SkyLine4Bot)\n" \
        + "Autor: Jordi Cluet Martinell\n" \
        + "Correu: jordi.cluet@upc.edu"
    sortida(update, context, text)


def lst(update, context):
    """Mostra els identificadors definits i la seva corresponent àrea."""
    try:
        ts = context.user_data['taula_simbols'] \
            if 'taula_simbols' in context.user_data else {}

        if not ts:
            text = "No hi ha cap identificador definit"
        else:
            text = "id -> àrea"
            for id, sky in ts.items():
                text += "\n" + str(id) + " -> " + str(sky.area())
        sortida(update, context, text)

    except Exception:
        text = "Hi ha hagut un error. Comprova la terminal."
        sortida(update, context, text)
        print(traceback.format_exc())
        print(sys.exc_info())


def clean(update, context):
    """Esborra tots els identificadors definits."""
    if 'taula_simbols' in context.user_data:
        context.user_data['taula_simbols'] = {}
    text = "Identificadors eliminats"
    sortida(update, context, text)


def save(update, context):
    """Guarda l'skyline id amb nom id.sky"""
    id = ' '.join(context.args)
    if 'taula_simbols' in context.user_data:
        ts = context.user_data['taula_simbols']
        if id in ts:
            sky = ts[id]
            nom = id + ".sky"
            escriu_pickle(sky, nom)
            text = "Skyline guardat com a " + nom
    else:
        text = "Aquest identificador no existeix"

    sortida(update, context, text)


def load(update, context):
    """Carrega l'skyline id de l’arxiu id.sky"""
    id = ' '.join(context.args)
    nom = id + ".sky"

    try:
        sky = llegeix_pickle(nom)
        if 'taula_simbols' not in context.user_data:
            context.user_data['taula_simbols'] = {}
        context.user_data['taula_simbols'][id] = sky
        text = "Skyline " + id + " carregat"

    except FileNotFoundError:
        text = "El fitxer " + nom + " no existeix"
    except Exception:
        text = "Error en carregar l'Skyline. Comprova la terminal"

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
    """Genera el gràfic de l'skyline i el guarda en un fitxer temporal."""
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

    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.bar(xs, hs, width=ws, align='edge', color=['red'])
    plt.savefig('tmp.png')
    plt.close()


class ParseError(Exception):
    """Classe per errors durant el parsejat"""
    pass


class MyErrorListener(ErrorListener):
    """Classe per controlar els errors al parser i llançar excepcions."""

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, *args):
        raise ParseError

    def reportAmbiguity(self, *args):
        raise ParseError

    def reportAttemptingFullContext(self, *args):
        raise ParseError

    def reportContextSensitivity(self, *args):
        raise ParseError


def entrada(update, context):
    """Parseja el missatge d'entrada, crea l'skyline i l'envia."""

    input_stream = InputStream(update.message.text)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    parser.addErrorListener(MyErrorListener())

    try:
        tree = parser.root()

        if 'taula_simbols' not in context.user_data:
            context.user_data['taula_simbols'] = {}
        visitor = EvalVisitor(context.user_data['taula_simbols'])

        (var, sk) = visitor.visit(tree)

        genera_grafic(sk)
        context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open('tmp.png', 'rb')
        )
        os.remove("tmp.png")

        sortida(update, context, "Àrea: " + str(sk.area()))
        sortida(update, context, "Alçada: " + str(sk.alcada()))

        context.user_data['taula_simbols'][var] = sk

    except ParseError:
        text = "Error en parsejar l'expressió."
    except KeyError:
        text = "Aquest identificador no existeix."
    except TypeError:
        text = "Error de tipus: operació no suportada."
    except Exception as err:
        text = "Hi ha hagut una excepció. Comprova la terminal."
        print(traceback.format_exc())
        print(sys.exc_info())

    sortida(update, context, text)


def sortida(update, context, text):
    """Envia el missatge text a l'usuari."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


# Constant amb l'access token del bot que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# Objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Indica que quan el bot rebi una comanda s'executi la funció corresponent
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('save', save))

# Permet que la funció entrada s'executi cada vegada que arriba un missatge
updater.dispatcher.add_handler(MessageHandler(Filters.text, entrada))

# Engega el bot
updater.start_polling()
