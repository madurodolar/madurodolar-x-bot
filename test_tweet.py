#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()

import os, tweepy, sys

# load only the four OAuth1 creds
consumer_key    = os.getenv("TW_API_KEY")
consumer_secret = os.getenv("TW_API_SECRET")
access_token    = os.getenv("TW_ACCESS_TOKEN")
access_secret   = os.getenv("TW_ACCESS_SECRET")

# sanity-check
for k,v in (
    ("TW_API_KEY",      consumer_key),
    ("TW_API_SECRET",   consumer_secret),
    ("TW_ACCESS_TOKEN", access_token),
    ("TW_ACCESS_SECRET",access_secret),
):
    if not v:
        print(f"ERROR: {k} is missing", file=sys.stderr)
        sys.exit(1)

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    wait_on_rate_limit=True
)

try:
    resp = client.create_tweet(text="🧪 Test tweet from my bot (manual run)")
    print("✅ Tweet sent, id:", resp.data["id"])
except Exception as e:
    print("❌ Error sending tweet:", e, file=sys.stderr)
    sys.exit(1)
