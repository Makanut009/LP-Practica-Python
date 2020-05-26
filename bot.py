# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

from Skyline import Skyline
import matplotlib.pyplot as plt

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

def counter(update, context):
    if 'counter' not in context.user_data:
        context.user_data['counter'] = 0
    context.user_data['counter'] += 1
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(context.user_data['counter']))

def load(update, context):
    id = ' '.join(context.args)
    sk = read_pickle(id + ".sky")
    xs = []
    alts = []
    for e in sk.edificis:
        xs += [i for i in range(e[0], e[2])]
        n = (e[2] - e[0])
        alts += [e[1]]*n

    print(len(xs), len(alts))
    
    try:
        plt.bar(xs, alts, width=1, align='edge', color=['red'])
        print("MAIAIAU")
        plt.savefig('plot.png')
        plt.close()
    except Exception as err:
        print(traceback.format_exc())
        print(sys.exc_info())
    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=id
    )

def save(update, context):
    id = ' '.join(context.args)
    sk = Skyline(2,3,4)
    write_pickle(sk, id + ".sky")
    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=id
    )


def read_pickle(filename: str):
    """Read object from pickle file."""
    with open(filename, "rb") as file:
        return pickle.load(file)


def write_pickle(obj: object, filename: str):
    """Save object in pickle file."""
    with open(filename, "wb") as file:
        return pickle.dump(obj, file)


visitor = EvalVisitor()

def aux(update, context):
    input_stream = InputStream(update.message.text)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    #visitor = EvalVisitor()
    
    try:
        (var, sk) = visitor.visit(tree)
    except KeyError:
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Aquest identificador no existeix")
    except TypeError:
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Error de tipus: operació no suportada")
    except Exception as err:
        print(traceback.format_exc())
        print(sys.exc_info())

    print("Var: ", var)

    print(len(sk.edificis))
    print(sk.edificis)

    xs = []
    alts = []
    for e in sk.edificis:
        xs += [i for i in range(e[0], e[2])]
        n = (e[2] - e[0])
        alts += [e[1]]*n

    print(len(xs), len(alts))
    
    try:
        plt.bar(xs, alts, width=1, align='edge', color=['red'])
        print("MAIAIAU")
        plt.savefig('plot.png')
        plt.close()
    except Exception as err:
        print(traceback.format_exc())
        print(sys.exc_info())
    

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
dispatcher.add_handler(CommandHandler('counter', counter))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('save', save))


updater.dispatcher.add_handler(MessageHandler(Filters.text, aux))

# engega el bot
updater.start_polling()