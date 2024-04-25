from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import logging
from weather_api import get_weather 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a city name, and I will send you the weather report.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Just send me a city name!')

def weather(update: Update, context: CallbackContext) -> None:
    city = update.message.text
    api_key = 'f28af951e85e978f03fbbb1c69c815c1'
    weather_data = get_weather(api_key, city)
    weather_report = f"Weather in {city}: {weather_data['weather'][0]['description']}, Temp: {weather_data['main']['temp']}°C"
    update.message.reply_text(weather_report)

def main():
    """Start the bot."""
    updater = Updater("6728571239:AAFJwYMeDxiQ937kWeppOCms2saFQlOlciU", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, weather))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
