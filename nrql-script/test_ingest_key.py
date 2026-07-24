import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

ingest_key = os.getenv("NEW_RELIC_LICENSE_KEY")
account_id = os.getenv("NEW_RELIC_ACCOUNT_ID")

if not ingest_key or not account_id:
    print("Missing NEW_RELIC_INGEST_KEY or NEW_RELIC_ACCOUNT_ID in .env")
    exit(1)

url = f"https://insights-collector.newrelic.com/v1/accounts/{account_id}/events"

headers = {
    "Api-Key": ingest_key,
    "Content-Type": "application/json"
}

event = [{
    "eventType": "IngestKeyTest",
    "source": "learning-claude-repo",
    "timestamp": datetime.now(timezone.utc).isoformat()
}]

response = requests.post(url, headers=headers, json=event)

print(f"Status code: {response.status_code}")
print(f"Response body: {response.text}")

if response.status_code == 200:
    print("\n✅ Ingest key works. Event accepted by New Relic.")
else:
    print("\n❌ Something went wrong. Check the status code/body above.")