import dotenv
import os

dotenv.load_dotenv()

class Config:
    MONGO_SETTINGS = {
        'user': os.environ['MONGO_USERNAME'],
        'pass': os.environ['MONGO_PASS'],
        'db': os.environ['MONGO_DB'],
        'host': os.environ['MONGO_HOST'],
        'port': os.environ['MONGO_PORT']
    }