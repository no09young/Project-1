import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client["project"]
coll = db.trainers

def load():
    x = str(input("What is the name of the JSON file?(Don't include the file extension in the name):"))
    y = str("D:\\Revature\\VSCode\\Python\\Project 1\\Foundation_Project\\trainerFolder\\")
    z = y + x
    with open(f"{z}" + ".json", "r") as file:
        data = json.load(file)
    name = data['name']
    
    title = data['title']
    
    type_check = False
    while type_check == False:
        type = data['type']
        with open("type.json", "r") as file2:
            attr = json.load(file2)
        for key in attr:
            if type == attr[key]:
                type_check = True
        if (type_check == False):
            print("Not a valid type.")
    #Team Check
    team = data['team']
    for mem in team:
        with open("pokedex.json", "r", encoding='utf=8') as file3:
            doc = json.load(file3)
            for x in doc:
                if mem == x['name']['english']:
                    pass
                
    
    mid = db.trainers.find_one({}, {"_id":-1})
    id = mid["_id"] + 1
    
    mid_srch = coll.find().sort('_id')
    for doc in mid_srch:
        pass
    mid = doc['_id']
    id = mid + 1
    
    doc = {"_id": id, "name": name, "title": title, "type": type, "team": team}
    #Write the resutls to the db creating a new doc
    in_id = db.trainers.insert_one(doc).inserted_id
    print(f"Trainer Registration Complete:\nID: {in_id}\nName: {name}\nTitle: {title}\nFavorite Type: {type}\nTeam: {team}")
    #give some 'ending process' statement