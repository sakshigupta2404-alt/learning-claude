import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

ACCOUNT_ID = os.getenv("NEW_RELIC_ACCOUNT_ID")
API_KEY = os.getenv("NEW_RELIC_USER_KEY")


# --- new code goes here ---
URL = "https://api.newrelic.com/graphql"

nrql_query = "SELECT count(*) FROM Transaction SINCE 1 day ago"

graphql_query = {
    "query": f"""
    {{
      actor {{
        account(id: {ACCOUNT_ID}) {{
          nrql(query: "{nrql_query}") {{
            results
          }}
        }}
      }}
    }}
    """
}
# Headers tell New Relic who we are and what format we're sending
headers = {
    "Content-Type": "application/json",
    "API-Key": API_KEY
}

# Send the actual request
response = requests.post(URL, json=graphql_query, headers=headers)

# Convert the response into a Python dictionary we can read
data = response.json()

print("Status code:", response.status_code)
print(data)