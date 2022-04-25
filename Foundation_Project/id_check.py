import json
from types import NoneType
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client["project"]

def id_check():
    id_check = False
    while(id_check == False):
        train_id = float(input("Please enter a Trainer ID:"))
        srch = db.trainers.find_one({"_id": train_id})
        
        if(train_id == 0):  #Will return the train_id as 0 still
            id_check = True
        elif(srch == None):
            print("ID not recognized. Please try again. (Enter 0 to quit)")
        else:
            id_check = True

    return train_id   

