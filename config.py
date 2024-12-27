from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7921939461:AAGOcCoi9yX8OjPmJs-jzaEEbAuwRZ_ufSA")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7086360370"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/1irotech/CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "ironmanhindigming"
UPDATE_CHNL = "irotechbotz0"
OWNER_USERNAME = "Ironmanhindigaming"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
