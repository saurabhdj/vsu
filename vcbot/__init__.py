import logging
import time
from pytgcalls import PyTgCalls
from pyrogram import Client
from vcbot.config import Var
from vcbot.queue import Queue

StartTime = time.time()

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("PyTgCalls").setLevel(logging.WARNING)
logging.getLogger("yt_dlp").setLevel(logging.WARNING)

queues = Queue()

Bot = None
if Var.BOT_TOKEN:
    Bot = Client(
        "bot",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        bot_token=Var.BOT_TOKEN,
        workers=2
    )
UB = Client(
    Var.SESSION,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    workers=8
)

group_calls = PyTgCalls(UB)
