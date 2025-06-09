import os
import tweepy
import requests

def get_price():
    # Aquí podrías llamar a tu endpoint público de madurodolar-web,
    # p. ej. https://www.madurodolar.com/price.json
    resp = requests.get("https://www.madurodolar.com/price.json")
    data = resp.json()
    return data["binance_p2p"]

def tweet(texto):
    client = tweepy.Client(
        bearer_token        = os.getenv("TW_BEARER_TOKEN"),
        consumer_key        = os.getenv("TW_API_KEY"),
        consumer_secret     = os.getenv("TW_API_SECRET"),
        access_token        = os.getenv("TW_ACCESS_TOKEN"),
        access_token_secret = os.getenv("TW_ACCESS_SECRET")
    )
    r = client.create_tweet(text=texto)
    print("Publicado:", r.data)

if __name__ == "__main__":
    precio = get_price()
    tweet(f"💡 Valor del dólar hoy en Venezuela: {precio} VES #MaduroDolar")
