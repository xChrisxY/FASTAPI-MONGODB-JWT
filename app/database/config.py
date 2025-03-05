from decouple import config

MONGO_URI = config("MONGO_URI", default="localhost")
PORT = config("PORT", default=27017, cast=int)
DATABASE_NAME = config("DATABASE_NAME")
COLLECTION_NAME = config("COLLECTION_NAME")