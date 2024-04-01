from dotenv import load_dotenv
import os

load_dotenv(override=True)

API_HASH = os.getenv("API_HASH")
API_ID = os.getenv("API_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PLUGINS = dict(root=os.getenv("PLUGINS_ROOT"))
PROXY = {"scheme": os.getenv("PROXY_SCHEME"),
         "hostname": os.getenv("PROXY_HOSTNAME"),
         "port": int(os.getenv("PROXY_PORT"))}
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DEBUG = os.getenv('DEBUG')
CACHE_TTL = int(os.getenv('CACHE_TTL'))
REDIS_DB = int(os.getenv('REDIS_DB'))