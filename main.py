import os

import telebot
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")

client = TelegramClient('session_name', api_id, api_hash)
client.start()

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"), parse_mode=None)

@client.on(events.NewMessage(chats=[int(os.environ.get("TRACK_CHAT_ID"))]))
async def handler(event):
    if os.environ.get("KEYWORD") in event.message.message:
      bot.send_message(os.environ.get("SEND_CHAT_ID"), event.message.message)

client.run_until_disconnected()
