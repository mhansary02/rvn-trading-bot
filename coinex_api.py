import requests
import os

API_KEY = os.getenv("COINEX_API_KEY")
API_SECRET = os.getenv("COINEX_API_SECRET")

def place_order(side, symbol):
    print(f"Simulated {side.upper()} order on {symbol}")
    # Actual CoinEx trading logic goes here
