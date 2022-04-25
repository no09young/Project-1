import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from id_check import *
import pprint


client = MongoClient()
db = client["project"]
coll = db.trainers

def delete():
    delete_check = False
    while(delete_check == False):
        temp = str(input(f"CAUTION: Do you want to delete a Trainer from the system?('Yes' to continue)"))
        if(temp == "Yes"):
            
            trainer_id = id_check()
            pprint.pprint(db.trainers.find_one({"_id": trainer_id}))

            temp_2 = str(input(f"Are you sure you want to delete Trainer {trainer_id} from the system?('Yes' to continue)"))
            if(temp_2 == "Yes"):
                #Delete trainer from system
                result = coll.delete_one({"_id": trainer_id})
                print(f"{result.deleted_count} trainer was removed from the system.")
                delete_check = True
            else:
                print("Stopping...")
                delete_check = True
                #exit the process
        else:
            print("Stopping...")
            delete_check = True
            #exit the process

