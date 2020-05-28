# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor
from antlr4.error.ErrorListener import ErrorListener

from Skyline import Skyline
import matplotlib.pyplot as plt
import pickle

import traceback

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Benvingut a SkyLineBot!\n" +
            "Usa /help per veure les comandes disponibles.")


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soc un bot amb les següents comandes:\n" +
            "/start: inicia la conversa amb el Bot\n" +
            "/author: escriu el nom i correu de l'autor\n" +
            "/lst: mostra els identificadors definits i la seva corresponent àrea\n" +
            "/clean: esborra tots els identificadors definits\n" +
            "/save id: guarda un skyline amb el nom id.sky\n" +
            "/load id: carrega un skyline de l’arxiu id.sky"
    )


def author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="SkylineBot\n" +
            "Autor: Jordi Cluet Martinell\n" +
            "Correu: jordi.cluet@upc.edu"
    )


def lst(update, context):
    
    if 'visitor' not in context.user_data:
        context.user_data['visitor'] = EvalVisitor()

    skys = context.user_data['visitor'].taula_simbols
    if not skys:
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "No hi ha cap identificador definit")
    else:
        msg = "id -> àrea"
        for id, sky in skys.items():
            msg += "\n" + id + " -> " + str(sky.area())
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = msg)


def clean(update, context):
    if 'visitor' in context.user_data:
        context.user_data['visitor'].taula_simbols = {}
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Identificadors eliminats")


def sortida(update, context, text):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = text
    )


def load(update, context):
    id = ' '.join(context.args)
    nom = id + ".sky"

    try:
        sky = read_pickle(nom)
        if 'visitor' not in context.user_data:
            context.user_data['visitor'] = EvalVisitor()
        context.user_data['visitor'].taula_simbols[id] = sky
        text = "Skyline " + id + " carregat"
        sortida(update, context, text)

    except FileNotFoundError:
        text = "El fitxer " + nom + " no existeix"
        sortida(update, context, text)


def save(update, context):
    id = ' '.join(context.args)

    simbols = {}
    if 'visitor' in context.user_data:
        simbols = context.user_data['visitor'].taula_simbols
        if id in simbols:
            sky = simbols[id]
            nom = id + ".sky"
            write_pickle(sky, nom)
            text = "Skyline guardat com a " + nom
            sortida(update, context, text)
            return

    text = "Aquest identificador no existeix"
    sortida(update, context, text)


def read_pickle(filename: str):
    """Read object from pickle file."""
    with open(filename, "rb") as file:
        return pickle.load(file)


def write_pickle(obj: object, filename: str):
    """Save object in pickle file."""
    with open(filename, "wb") as file:
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


class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
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
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Error en parsejar l'expressió. Comprova la terminal")
        raise

    try:
        if 'visitor' not in context.user_data:
            context.user_data['visitor'] = EvalVisitor()
        (var, sk) = context.user_data['visitor'].visit(tree)
        genera_grafic(sk)

    except KeyError:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Aquest identificador no existeix")
        raise
    except TypeError:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Error de tipus: operació no suportada")
        raise
    except Exception as err:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Hi ha hagut una excepció. Comprova la terminal")
        print(traceback.format_exc())
        print(sys.exc_info())
        raise

    # print("Var: ", var)
    # print("Nombre d'edificis: ", len(sk.edificis))
    # print("Edificis: ", sk.edificis)

    context.bot.send_photo(chat_id = update.message.chat_id, photo = open('plot.png', 'rb'))
    context.bot.send_message(chat_id = update.effective_chat.id, text = ("area: " + str(sk.area())))
    context.bot.send_message(chat_id = update.effective_chat.id, text = "alçada: " + str(sk.alcada()))
    

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