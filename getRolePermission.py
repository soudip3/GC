import requests, sys
from dotenv import dotenv_values
from authorization import authentication
from loadExcel import loadExcel

ACCESS_TOKEN_JSON = authentication()

def getRolePermission(role):
    credentials =  dotenv_values(".env")
    ENVIRONMENT = credentials["GENESYS_CLOUD_ENVIRONMENT"]
    request_headers = {
        "Authorization": f"{ ACCESS_TOKEN_JSON['token_type'] } { ACCESS_TOKEN_JSON['access_token']}"
    }

    response = requests.get(f"https://api.{ENVIRONMENT}//api/v2/authorization/roles?name={role}",headers=request_headers)

    if response.status_code==200:
        response_json = response.json()
        loadExcel(response_json,role)
    else:
        print(f"Failure: { str(response.status_code) } - { response.reason }")
        sys.exit(response.status_code)
