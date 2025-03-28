
import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7062691808:AAFittmoSJm7gaR2ME_zhyUik6YXuJ3xeoM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26205215"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d4d9b7bce6d76bec759e404ecf2c3ebf")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002141494142"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1178233430"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ZahidNazir:ZahidNazir@1stcluster.1p0dlne.mongodb.net/?retryWrites=true&w=majority&appName=1stcluster")
DB_NAME = os.environ.get("DATABASE_NAME", "ZahidNazir")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002065254823"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {username}\n\nI Am File store Bot Created by @tactition I Store Files So other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6852649461").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join Our Community to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{previouscaption} \n <b>@Self_Improvement_Audiobooks</b>" )

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "true") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages! You Can't Use Me. I am only meant For @tactition."

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
