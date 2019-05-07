import telebot

bot_token = " "
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(content_types=['text'])
def handle_command(message):
    length = len(message.text)
    input_string = message.text
    if input_string[length - 1] in 'ьЬтТаоеяуёэыиАОЕЯУЁЭЫИцЦ':
        if input_string[length - 1] in 'ьЬ':
            bot.send_message(message.chat.id, message.text + "ша")
        if input_string[length - 1] in 'тТ':
            bot.send_message(message.chat.id, message.text + "щица")
        if input_string[length - 1] in 'аоеяуёэыиАОЕЯУЁЭЫИ':
            bot.send_message(message.chat.id, message.text + "рка")
        if input_string[length - 1] in 'цЦ':
            str1 = input_string[0:length - 2:1]
            bot.send_message(message.chat.id, str1 + "чиха")
    else:
        bot.send_message(message.chat.id, message.text + "иня")


bot.polling(none_stop=True, interval=0)
