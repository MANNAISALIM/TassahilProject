import pymongo
import json


def getFromMongo():
    client = pymongo.MongoClient("127.0.0.1", 27017)
    #print("Connection Successful")
    db = client["JobsIndustry"]
    collection = db["AllJobsIndustry"]
    team = {}
    for x in collection.find({"JobTitle" :{ "$eq" : "AI developer" }}, { "_id":0}):
        team = x

    #print("Connection closed")
    return (team)
    client.close()
