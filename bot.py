# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

from skyline import Skyline

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
            "/counter id: carrega un skyline de l’arxiu id.sky"
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


visitor = EvalVisitor()

def aux(update, context):
    input_stream = InputStream(update.message.text)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    #visitor = EvalVisitor()
    sk = Skyline()
    (var, sk) = visitor.visit(tree)
    print("VaR: ", var)
    
    try:
        sk.mostra()
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        print(traceback.format_exc())
        # or
        print(sys.exc_info())

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

updater.dispatcher.add_handler(MessageHandler(Filters.text, aux))

# engega el bot
updater.start_polling()



    # try:
    #     tree = parser.root()
    # except Exception as err:
    #     traceback.print_tb(err.__traceback__)
    #     print(traceback.format_exc())
    #     # or
    #     print(sys.exc_info())
