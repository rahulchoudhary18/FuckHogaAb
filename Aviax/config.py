# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Aviax/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 2984107  # integer value, dont use ""
    API_HASH = "4ce83ad7d954da391c659c6d7d76e0ce"
    TOKEN = "5036420078:AAHmWN2OTHhae-8MPfBi7hB2JUtzJxHKolU"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1689542319  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "RahulChoudhary17"
    SUPPORT_CHAT = "AviaxSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001633114368
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001633114368
    )  # Prints info rmation like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    DB_URL = "postgresql://jdzcyyju:7tHwBXlUlK9UCKAtsgVxA5d9aGUzar9g@arjuna.db.elephantsql.com/jdzcyyju"  # needed for any database modules # its "URI" and not "URL" as heroku and similar ones only accept it as such
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    STRICT_GBAN = False
    MONGO_DB_URL = "mongodb+srv://userbot:userbot@cluster0.ooedq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    REDIS_URL = "redis://AviaxRedisOp:Rahulrahul11111_@redis-18183.c10.us-east-1-4.ec2.cloud.redislabs.com:18183/AviaxRedisOp"
    
    SPAMWATCH_SUPPORT_CHAT = "@AviaxSupport"
    SPAMWATCH_API = "xpKDzGXxXksbRFYrQGKH3445Ex0fEMegtptlwXTIMoKXuZ2NpZZt1aLQji8kgeEm"
    REM_BG_API_KEY = "qtCcZRxigrDt1pZ4E1PQrQnG"
    OPENWEATHERMAP_ID = "6b9b233c98ae2a761758fb1e45e9491d"
    BOT_ID = "5036420078"
    BOT_USERNAME = "AviaxBeatzBot"
    GENIUS_API_TOKEN = None
    YOUTUBE_API_KEY = "AIzaSyBvAVCNGGDsloQKf_FR_JLtrFp5n9AN3Lw"
    ARQ_API_URL = "https://thearq.tech"
    GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
    CHROME_DRIVER = "/usr/bin/chromedriver"
    BOT_NAME = "Aviax"
    DEL_CMDS = False
    MONGO_DB = "Aviax"
    BOT_API_URL = "https://api.telegram.org/bot"
    HELP_IMG = "https://telegra.ph/file/d05a3ce6f08404cd88361.jpg"
    START_IMG = "https://telegra.ph/file/d05a3ce6f08404cd88361.jpg"
    AVIAX_PHOTO = "https://telegra.ph/file/d05a3ce6f08404cd88361.jpg"
    APP_ID = 2984107
    APP_HASH = "4ce83ad7d954da391c659c6d7d76e0ce"
    STRING_SESSION = "1AZWarzkBu0Sm3q2FAyFAIiwVoVW9Qz12K2-n-F54UTiqs2zML4w1RghJ98xRGcs92JLWjOM8xcgw0CaupOCyP93gYcZJDjzGIrRDN84x1huJ2jUOKQZb9wpTe2tWpoVb-XF0d0JWPMuX3LNUD0UPr4QYOalNkJ1iNxwZ3exSCoqKMsNMwBk-Ulr5vSvkoVMfzGA2jSBKiTJJAclxL4aSv0tuEbA_0rNkW7uIYOkBi91ihPaLxDIiRa7rncL6I4oo5UoBTMhnHtyi-TjCkAcCum2rP5uNuJ5ahGOt7LgeNs_hPTQlZd4InZoAiuC3S97XuiImYZZ6GwhNlVYF92Nw7G9d9Dzi8yY="

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
