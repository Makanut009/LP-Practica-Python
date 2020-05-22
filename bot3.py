# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    print(update)
    print(context)
    botname = context.bot.username
    username = update.effective_chat.username
    fullname = update.effective_chat.first_name + ' ' + update.effective_chat.last_name
    missatge = "Tu ets en %s (%s) i jo soc el %s." % (fullname, username, botname)
    context,bot.send_message(chat_id=update.effective_chat.id, text=missatge)

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()
# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi una comanda s'executi la funció corresponent
dispatcher.add_handler(CommandHandler('start', start))

# engega el bot
updater.start_polling()