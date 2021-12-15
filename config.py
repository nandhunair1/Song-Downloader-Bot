import os

class Config(object):
    DATABASE = os.environ.get("DB_URI")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1961162381").split())
    SUPPORT = os.environ.get("SUPPORT")
    PICS = os.environ.get("PICS", "https://telegra.ph/file/3cddff05c6461a471af4c.jpg")).split()

