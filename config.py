import os

class Config(object):
    DATABASE = os.environ.get("DB_URI")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1961162381").split())
    SUPPORT = os.environ.get("SUPPORT")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/0254a014cb78c3cca2df0.jpg")

