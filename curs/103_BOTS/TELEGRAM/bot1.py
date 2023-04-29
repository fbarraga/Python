# importa l'API de Telegram
from telegram.ext import Application, CommandHandler,ContextTypes
from telegram import Update

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
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
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()