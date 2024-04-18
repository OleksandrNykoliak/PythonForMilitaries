import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, "Got your photo")

    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as my_image:
        my_image.write(downloaded_file)

    bot.send_message(message.chat.id, "Saved your photo")
    bot.send_photo(message.chat.id, open('image.jpg', 'rb'))


bot.infinity_polling()




# https://pypi.org/project/pyTelegramBotAPI/