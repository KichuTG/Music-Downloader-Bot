# © Cyril C Thomas
# https://t.me/cyril_c_10

import os

class Config(object):
    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1905251964")
    API_ID = int(os.environ.get("APP_ID", "28714959"))
    API_HASH = os.environ.get("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001678094109))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    SESSION_NAME = os.environ.get("SESSION_NAME", "spotdown")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
