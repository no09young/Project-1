import json
import pprint
from id_check import *
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client["project"]

def view():
    train_id = id_check()
    if (train_id > 0):
        #select info for trainer temp
        pprint.pprint(db.trainers.find_one({"_id": train_id}))
    else:
        print("Stopping")
    #give some 'ending process' statement