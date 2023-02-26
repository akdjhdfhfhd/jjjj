from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/22394c2ebaf52272be4da.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/22394c2ebaf52272be4da.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ah_9_v")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ah07v")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://telegra.ph/file/22394c2ebaf52272be4da.jpg"
