import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1658f5d92eaefd8dea45f.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/2dc19950129e718fcfe4a.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/ed39ffcad887bb4b8408d.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c3f490ae4e81d1c258cad.jpg")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/dd48463d45b62c53aa860.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/731100f6dd07e75a7872b.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "OctavePlugin")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Rockerz_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Xmarty_Support")
# fill here ur owner id username without @
OWNER_NAME = getenv("OWNER_NAME", "Xmartperson")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "Salim")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/S780821/Rockerz_Muzic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
