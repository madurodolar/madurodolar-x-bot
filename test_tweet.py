#!/usr/bin/env python3
from dotenv import load_dotenv
import os, sys, tweepy

# 1) Load .env
loaded = load_dotenv()
print("DEBUG: load_dotenv() →", loaded, file=sys.stderr)

# 2) Print out exactly what each TW_* var is
for name in ("TW_API_KEY","TW_API_SECRET","TW_ACCESS_TOKEN","TW_ACCESS_SECRET","TW_BEARER_TOKEN"):
    val = os.getenv(name)
    print(f"DEBUG: {name} = {repr(val)}", file=sys.stderr)

# 3) Sanity‐check
missing = [n for n in ("TW_API_KEY","TW_API_SECRET","TW_ACCESS_TOKEN","TW_ACCESS_SECRET") if not os.getenv(n)]
if missing:
    print("❌ Missing credentials:", missing, file=sys.stderr)
    sys.exit(1)

# 4) Try the tweet
client = tweepy.Client(
    consumer_key        = os.getenv("TW_API_KEY"),
    consumer_secret     = os.getenv("TW_API_SECRET"),
    access_token        = os.getenv("TW_ACCESS_TOKEN"),
    access_token_secret = os.getenv("TW_ACCESS_SECRET"),
    wait_on_rate_limit  = True
)

try:
    resp = client.create_tweet(text="🧪 Test tweet from my bot")
    print("✅ Tweet sent, id:", resp.data["id"])
except Exception as e:
    print("❌ Error sending tweet:", e, file=sys.stderr)
    sys.exit(1)
