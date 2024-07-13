from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("CLIENT_ID"))
print(os.getenv("CLIENT_SECRET"))