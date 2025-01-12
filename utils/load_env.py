import os
from dotenv import load_dotenv

load_dotenv()
cg_api_key = os.getenv("CG_API_KEY")
binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_secret")
