from dotenv import dotenv_values

credentials_dev =  dotenv_values(".env.dev")

print(credentials_dev["CLIENT_ID"])
print(credentials_dev["CLIENT_SECRET"])