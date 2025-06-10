#!/usr/bin/env python3
from dotenv import load_dotenv
import os, sys, tweepy

# Carga explícita de .env si no está en el cwd:
load_dotenv()

# Verifica que las vars estén presentes
for name in ("TW_API_KEY","TW_API_SECRET","TW_ACCESS_TOKEN","TW_ACCESS_SECRET"):
    if not os.getenv(name):
        print(f"❌ Falta {name}", file=sys.stderr)
        sys.exit(1)

client = tweepy.Client(
    consumer_key=        os.getenv("TW_API_KEY"),
    consumer_secret=     os.getenv("TW_API_SECRET"),
    access_token=        os.getenv("TW_ACCESS_TOKEN"),
    access_token_secret= os.getenv("TW_ACCESS_SECRET"),
    wait_on_rate_limit=True
)

try:
    resp = client.create_tweet(text="🧪 Test tweet desde mi bot")
    print("✅ Tweet enviado! ID:", resp.data["id"])
except Exception as e:
    print("❌ Error enviando tweet:", e, file=sys.stderr)
    sys.exit(1)
