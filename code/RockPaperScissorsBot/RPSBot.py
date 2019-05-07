import time

import telebot
from telebot import types
from telebot.apihelper import ApiException
from random import randint

bot_token = " "
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Let\'s play', reply_markup=keyboard())


@bot.message_handler(content_types=['text'])
def handle_command(message):
    bot_turn = randint(0, 2)
    print_bot_turn(bot_turn, message)
    user_turn = get_user_turn(message)
    play(user_turn, bot_turn, message)


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button0 = types.KeyboardButton('Rock')
    button1 = types.KeyboardButton('Paper')
    button2 = types.KeyboardButton('Scissors')
    markup.add(button0)
    markup.add(button1)
    markup.add(button2)
    return markup


def get_user_turn(message):
    if message.text == 'Rock':
        return 0
    elif message.text == 'Paper':
        return 1
    elif message.text == 'Scissors':
        return 2
    else:
        return -1


def print_bot_turn(turn_id, message):
    if turn_id == 0:
        bot.send_message(message.chat.id, 'Rock')
    if turn_id == 1:
        bot.send_message(message.chat.id, 'Paper')
    if turn_id == 2:
        bot.send_message(message.chat.id, 'Scissors')


def play(user_turn, bot_turn, message):
    if user_turn == -1:
        bot.send_message(message.chat.id, 'I don\'t get it')
    else:
        game_matrix = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
        if game_matrix[user_turn][bot_turn] == 0:
            bot.send_message(message.chat.id, 'Draw')
        elif game_matrix[user_turn][bot_turn] == 1:
            bot.send_message(message.chat.id, 'I win')
        else:
            bot.send_message(message.chat.id, 'You win')


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except ApiException:
        time.sleep(15)
