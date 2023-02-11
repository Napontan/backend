from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(".env")

mongo_user = os.getenv("usernamee")
mongo_paswd = os.getenv("password")
mongo_host = os.getenv("host")
mongo_port = os.getenv("port")

client = MongoClient(f"mongodb://{mongo_user}:{mongo_paswd}@{mongo_host}:{mongo_port}")
db = client["exceed15"]
collection = db["enrollment"]
 
print(client.list_database_names())

