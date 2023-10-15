import telebot
import json
import pyautogui as pg
import os


def tg_msg(message):
    try:
        bot.send_message(tg_id, message)
    except Exception as ex:
        pass



def send_screen():
    try:
        pg.screenshot('data/settings/screen.png')
        photo = open('data/settings/screen.png', 'rb')
        bot.send_photo(tg_id, photo)
        photo.close()
        os.remove('settings/screen.png')
    except Exception as ex:
        tg_msg('Error')


with open('data/settings/settings.json', 'r', encoding='utf=8') as file:
    data = json.load(file)
    tg_token = data['telegram_token']
    tg_id = data['your_telegram_id']
    bot_state = data['is_bot_active']
    if bot_state == 'on':
        bot = telebot.TeleBot(tg_token)
        tg_msg('The program starts working')
