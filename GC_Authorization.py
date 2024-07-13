import requests, base64, sys
from dotenv import dotenv_values

credentials =  dotenv_values(".env.dev")
CLIENT_ID = credentials["GENESYS_CLOUD_CLIENT_ID"]
CLIENT_SECRET = credentials["GENESYS_CLOUD_CLIENT_SECRET"]
ENVIRONMENT = credentials["GENESYS_CLOUD_ENVIRONMENT"]

encodedData = base64.b64encode(bytes(f"{CLIENT_ID}:{CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")

request_headers = {
    "Authorization": f"Basic {encodedData}",
    "Content-Type": "application/x-www-form-urlencoded"
}

request_body = {
    "grant_type": "client_credentials"
}

def authentication():
    response = requests.post(f"https://login.{ENVIRONMENT}/oauth/token", data=request_body, headers=request_headers)
    if response.status_code==200:
        response_json = response.json()
        return response_json
    else:
        print(f"Failure: { str(response.status_code) } - { response.reason }")
        sys.exit(response.status_code)