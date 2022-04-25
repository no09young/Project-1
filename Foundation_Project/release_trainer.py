import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from id_check import *

client = MongoClient()
db = client["project"]
coll = db.trainers

def release():
    train_id = id_check()
    #make sure the pokemon is removed from the appropriate trainer team
    srch = coll.find_one({"_id": train_id})
    #set team[] equal to results
    team = srch["team"]

    release_check = False
    while release_check == False:
        team1 = team.copy()
        print(f"Your current team is {team1}")
        if (len(team) > 0):
            temp = str(input("Who would you like to release(0 to stop)?"))
            if(temp in team1):
                x = team.index(temp)
                print(f"{team.pop(x)} has been released.")
            elif(temp == "0"):
                print("Stopping...")
                release_check = True
            else:
                print(f"{temp} was not found on the team.")
        else:
            print(f"There are no Pokemon to release. Please Catch a Pokemon first.")
            release_check = True
    coll.update_one({"_id": train_id}, {"$set": {"team": team}})
    #give some 'ending process' statement