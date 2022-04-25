import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from id_check import *

client = MongoClient()
db = client["project"]
coll = db.trainers

def catch():
    train_id = id_check()
    #make the sure the functions add the pokemon to the appropriate trainer team
    srch = coll.find_one({"_id": train_id})
    #set team[] equal to results
    team = srch["team"]
    team_check = False
    while team_check == False:
        team1 = team.copy()
        print(f"Current team is {team1}")
        if(len(team) < 6):
            temp = str(input("Enter a Pokemon to capture('0' to stop):"))
            with open("pokedex.json", "r", encoding='utf=8') as file:
                doc = json.load(file)
            if(temp != '0'):
                for x in doc:
                    if temp == x['name']['english']:
                        team.append(temp)
            else:
                print('stoppping')
                team_check = True
            
            if(len(team) == len(team1) and temp != '0'):
                print("Pokemon name not recognized")
        else:
            print(f"Team is full. Cannot have more than 6 Pokemon on a team. Please Release a Pokemon before adding more.")
            team_check = True
 
    coll.update_one({"_id": train_id}, {"$set": {"team": team}})
    print(f" Your team is currently: {team}")
    #give some 'ending process' statement
