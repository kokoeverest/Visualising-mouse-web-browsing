import pymongo
import os

USER = os.getenv("MONGODB_USERNAME")
PASSWD = os.getenv("MONGODB_PASSWORD")

def db_init():
    dbclient = pymongo.MongoClient(f"mongodb://{USER}:{PASSWD}@localhost:27017/")
    images_db = dbclient["imagesdb"]
    images_collection = images_db["events"]

    return images_collection


database = db_init()