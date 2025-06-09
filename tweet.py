#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()     # ← this pulls in TW_API_* from your local .env
import os
import tweepy
import requests
import sys

def get_price():
    # Or just return a fixed test value to prove the tweet path works:
    # return "TEST-PRICE"
    resp = requests.get("https://www.madurodolar.com/price.json")
    print("get_price() HTTP status:", resp.status_code, file=sys.stderr)
    data = resp.json()
    precio = data.get("binance_p2p")
    print("Price fetched:", precio, file=sys.stderr)
    return precio

def tweet(texto: str):
    # Print out the vars the script sees:
    for name in ("TW_API_KEY","TW_API_SECRET","TW_ACCESS_TOKEN","TW_ACCESS_SECRET","TW_BEARER_TOKEN"):
        print(f"{name} =", os.getenv(name), file=sys.stderr)
    client = tweepy.Client(
        bearer_token        = os.getenv("TW_BEARER_TOKEN"),
        consumer_key        = os.getenv("TW_API_KEY"),
        consumer_secret     = os.getenv("TW_API_SECRET"),
        access_token        = os.getenv("TW_ACCESS_TOKEN"),
        access_token_secret = os.getenv("TW_ACCESS_SECRET"),
        wait_on_rate_limit  = True
    )
    try:
        resp = client.create_tweet(text=texto)
        print("Tweepy response:", resp, file=sys.stderr)
        print("Publicado:", resp.data)
    except Exception as e:
        print("Error tweeting:", e, file=sys.stderr)

if __name__ == "__main__":
    precio = get_price()
    print("DEBUG: precio =", precio, file=sys.stderr)
    for name in ("TW_API_KEY","TW_API_SECRET","TW_ACCESS_TOKEN","TW_ACCESS_SECRET","TW_BEARER_TOKEN"):
        print(f"DEBUG: {name} →", os.getenv(name), file=sys.stderr)

    tweet(f"💡 Valor del dólar hoy en Venezuela: {precio} VES #MaduroDolar")

