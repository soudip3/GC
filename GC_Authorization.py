import requests
import base64
import sys
from dotenv import dotenv_values

credentials_dev =  dotenv_values(".env.dev")
client_id = credentials_dev["GENESYS_CLOUD_CLIENT_ID"]
client_secret = credentials_dev["GENESYS_CLOUD_CLIENT_SECRET"]
access_token_url = credentials_dev["GENESYS_CLOUD_ACCESS_TOKEN_URL"]
encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")

request_headers = {
    "Authorization": f"Basic {encodedData}",
    "Content-Type": "application/x-www-form-urlencoded"
}

request_body = {
    "grant_type": "client_credentials"
}

response = requests.post(credentials_dev["GENESYS_CLOUD_ACCESS_TOKEN_URL"], data=request_body, headers=request_headers)

if response.status_code==200:
    response_json = response.json()
    access_token = response_json['access_token']
else:
    print(f"Failure: { str(response.status_code) } - { response.reason }")
    sys.exit(response.status_code)