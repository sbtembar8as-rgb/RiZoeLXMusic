from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("8709552170:AAELuLrOYtjCe02IK_Nv3fndv_yl10gSqqg")
BOT_NAME = getenv("ميوزك")

API_ID = int(getenv("38841029"))
API_HASH = getenv("289dc5614e276b770dfc5718fcd9248d")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("8172514055").split()))
