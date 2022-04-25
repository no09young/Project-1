import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client["project"]
coll = db.trainers

def create():

    name = str(input(f"Please enter a name:"))
    
    title = str(input(f"Please enter a title:"))
    
    type_check = False
    while type_check == False:
        type = str(input(f"Please enter favorite type:"))
        with open("type.json", "r") as file:
            attr = json.load(file)
        for key in attr:
            if type == attr[key]:
                type_check = True
        if (type_check == False):
            print("Not a valid type.")
    
    mid_srch = coll.find().sort('_id')
    for doc in mid_srch:
        pass
    mid = doc['_id']
    id = mid + 1
    
    doc = {"_id": id, "name": name, "title": title, "type": type, "team": []}
    #Write the resutls to the db creating a new doc
    in_id = db.trainers.insert_one(doc).inserted_id
    print(f"Trainer Registration Complete:\nID: {in_id}\nName: {name}\nTitle: {title}\nFavorite Type: {type}")
    #give some 'ending process' statement