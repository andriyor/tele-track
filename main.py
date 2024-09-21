import os

import telebot
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
TG_TOKEN = os.environ.get("TG_TOKEN")
TRACK_CHAT_ID = os.environ.get("TRACK_CHAT_ID")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
KEYWORD = os.environ.get("KEYWORD")
SEND_CHAT_ID = os.environ.get("SEND_CHAT_ID")

client = TelegramClient('session_name', API_ID, API_HASH)
client.start()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@client.on(events.NewMessage(chats=[int(TRACK_CHAT_ID)]))
async def handler(event):
    if any(keyword in event.message.message for keyword in KEYWORD.split(',')):
      bot.send_message(SEND_CHAT_ID, event.message.message)

client.run_until_disconnected()
