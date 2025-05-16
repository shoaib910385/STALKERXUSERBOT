import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = getenv("OWNER_ID", "7659846392")
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://files.catbox.moe/rz44me.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/shoaib910385/STALKERXUSERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1sBu5xqqGQzbScTlqoHAF7orhCEpBXUIL5hklAhi830CKhWRj99tbOWBFOM0JFz29YPPCNkJhM2A8ycpNvSH0JJO5H1Ocw84NgXiGM348ijDSHVi3XxK_FnPVDoItAuKZxL9sBlKcR3Uz0OJnIZJ7lFXbntx1DHhQE-mQ9sGJkxr1JqAzgfV3kghqvzig62sdley2w6rL1KLpraayVjDkZEpUMUut-i7nVLTWJaePgNYr19miiwq-6Jk0WgozQDE_r2x6TjHQUGjoz9Szhf5PLg_U702wM-g3zfv2Md6wkdI_sxaPEfeaTYVQXey4nISVil0BklmyLJCsElRfjsyINS2KY=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
