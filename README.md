# Foundation Project/Project 1
## Description
A Python CLI (Command Line Inteface) application to showcase CRUD functionality between Python and MongoDB.
Theme is based on Nintendo popular game series Pokemon.
The application allows the use to create a Trainer, load in trainer information from a JSON file, add and remove
  pokemon from the trainer's team, view trainer information, and delete a trainer from the database.
## Technologies Used
  - Python 3
  - MongoDB
  - PyMongo
## Features and Future Improvements
Features:  
  - Includes full list of Pokemon up to generation 7
  - Allows for changing of team composition
  
Future Improvements:
  - Fix code to work when the database is empty (has no records)
  - Add a functionality to view all the Trainers in the database
  - Add error handling to the code
  - Format the output to make it more reader friendly
  - Organize the Github Repository to make it more user friendly


## To Use:
  - Start MongoDB server in it's own terminal window with: mongod.exe
    - Currently requires a record with "_id": 1 present for initial use
  - Start the program in it's own terminal window with: python start.py
  - Any .json files to be loaded must be in the same directory as the application.
    - .json should contain the following keys: "name", "title", "type", "team"
    - "team" value should be a list ("team": [])
    - the name of the .json should be the same as the "name" value (Nick.json and "name": Nick)
## License
This project uses the following license: MIT
