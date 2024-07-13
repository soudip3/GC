import requests, sys
from dotenv import dotenv_values
from GC_Authorization import authentication
from GC_LoadRoletoExcel import loadExcel

ACCESS_TOKEN_JSON = authentication()
credentials =  dotenv_values(".env.dev")
ENVIRONMENT = credentials["GENESYS_CLOUD_ENVIRONMENT"]
request_headers = {
    "Authorization": f"{ ACCESS_TOKEN_JSON['token_type'] } { ACCESS_TOKEN_JSON['access_token']}"
}

response = requests.get(f"https://api.{ENVIRONMENT}/api/v2/authorization/roles/{sys.argv[1]}",headers=request_headers)

if response.status_code==200:
    response_json = response.json()
    loadExcel(response_json)
else:
    print(f"Failure: { str(response.status_code) } - { response.reason }")
    sys.exit(response.status_code)
