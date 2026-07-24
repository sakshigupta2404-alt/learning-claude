import os
import time
import random
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

license_key = os.getenv("NEW_RELIC_LICENSE_KEY")
account_id = os.getenv("NEW_RELIC_ACCOUNT_ID")

if not license_key or not account_id:
    print("Missing NEW_RELIC_LICENSE_KEY or NEW_RELIC_ACCOUNT_ID in .env")
    exit(1)

url = f"https://insights-collector.newrelic.com/v1/accounts/{account_id}/events"
headers = {
    "Api-Key": license_key,
    "Content-Type": "application/json"
}

PRODUCTS = ["Wireless Mouse", "Coffee Mug", "Notebook", "Desk Lamp", "Backpack"]
USERS = [f"user_{i}" for i in range(1, 11)]

def make_event():
    event_type = random.choice(["OrderPlaced", "PageView"])
    base = {
        "eventType": event_type,
        "userId": random.choice(USERS),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "docker-custom-events-app"
    }
    if event_type == "OrderPlaced":
        base["product"] = random.choice(PRODUCTS)
        base["price"] = round(random.uniform(5, 150), 2)
        base["quantity"] = random.randint(1, 3)
    else:
        base["page"] = random.choice(["/home", "/product", "/cart", "/checkout"])
    return base

def send_event(event):
    response = requests.post(url, headers=headers, json=[event])
    print(f"Sent {event['eventType']} | Status: {response.status_code}")

if __name__ == "__main__":
    print("Starting custom-events generator. Sending one event every 10 seconds...")
    while True:
        event = make_event()
        send_event(event)
        time.sleep(10)