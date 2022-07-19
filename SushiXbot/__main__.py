import requests
from pyrogram import Client as Bot

from SushiXbot.config import API_HASH
from SushiXbot.config import API_ID
from SushiXbot.config import BG_IMAGE
from SushiXbot.config import BOT_TOKEN
from SushiXbot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="SushiXbot.modules"),
)

bot.start()
run()
