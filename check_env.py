from dotenv import load_dotenv
import os, sys

# Carga explícita:
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if not load_dotenv(dotenv_path):
    print(f"⚠️ No se cargó {dotenv_path}", file=sys.stderr)

for name in ("TW_API_KEY","TW_API_SECRET","TW_ACCESS_TOKEN","TW_ACCESS_SECRET","TW_BEARER_TOKEN"):
    print(name, "→", repr(os.getenv(name)))