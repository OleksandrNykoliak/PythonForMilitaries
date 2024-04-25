from json import load
import telebot
import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUR_BOT_TOKEN = os.getenv('YOUR_BOT_TOKEN')
API_KEY = os.getenv('API_KEY')


def get_weather(API_KEY, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()




bot = telebot.TeleBot(YOUR_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Введіть будь ласка місто, погоду якого ви хочете дізнатись: ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    import datetime
    city = message.text
    weather_data = get_weather(API_KEY, city)
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    windy = weather_data['wind']['speed']
    clouds = weather_data['clouds']['all']
    sunrise = datetime.datetime.fromtimestamp(
        weather_data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(
        weather_data['sys']['sunset']).strftime('%H:%M:%S')
    bot.reply_to(message, f'Погода у місті {city}:\n'
                          f'Опис: {description}\n'
                          f'Температура: {temperature}°C\n'
                          f'Швидкість вітру: {windy} м/с\n'
                          f'Хмарність: {clouds}%\n'
                          f'Схід сонця: {sunrise}\n'
                          f'Захід сонця: {sunset}')

bot.infinity_polling()
