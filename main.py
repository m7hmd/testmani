import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "5246967732:AAETJ1mWBcrWODHYjcNY6yEnC2leg6yR3NA"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
def reb(w, message):
    arr = []
    if len(w) == 3:
        arr.append(f"{w[0]}{w[0]}{w[0]}{w[1]}{w[2]}")
        arr.append(f"{w[0]}{w[1]}{w[1]}{w[1]}{w[2]}")
        arr.append(f"{w[0]}{w[1]}{w[2]}{w[2]}{w[2]}")
        bot.send_message(message.chat.id, "\n".join(arr))
    elif len(w) == 4:
        arr.append(f"{w[0]}{w[0]}{w[1]}{w[2]}{w[3]}")
        arr.append(f"{w[0]}{w[1]}{w[1]}{w[2]}{w[3]}")
        arr.append(f"{w[0]}{w[1]}{w[2]}{w[2]}{w[3]}")
        arr.append(f"{w[0]}{w[1]}{w[2]}{w[3]}{w[3]}")
        bot.send_message(message.chat.id, "\n".join(arr))
    else:
        bot.send_message(message.chat.id, 'حجي هاي مو رباعيه ولا ثلاثيه')
@bot.message_handler(content_types=['text'])
def send(message):
    if "/" in message.text:
        bot.send_message(message.chat.id, "هلا حجي ....")
    else:
        reb(message.text, message)
   
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://listmakerfz.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
