import pymongo
from flask import jsonify
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["questions"]
mycol = mydb["questions"]

result = None

with open('tmmQuestions.json') as f:
    result = json.load(f)

if result is not None:
    for question in result["questions"]:
        x = mycol.insert_one(question)
        print (x)
