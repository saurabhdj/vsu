from os import path, getenv, environ
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class Var(object):
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = getenv('BOT_TOKEN')
    BOT_USERNAME = getenv("BOT_USERNAME", "veezvidstreambot")
    SESSION = str(getenv('SESSION'))
    SUDO =  list(int(x) for x in getenv('SUDO', '').split())
    FPS = int(getenv('FPS', 20))
    WIDTH = int(getenv('WIDTH', 854))
    HEIGHT = int(getenv('HEIGHT', 480))
    BITRATE = int(getenv('BITRATE', 48000))
