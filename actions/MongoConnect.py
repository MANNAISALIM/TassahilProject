import pymongo
import json


def getWebinarDetailsFromMongo():
    client = pymongo.MongoClient("127.0.0.1", 27017)
    #print("Connection Successful")
    db = client["Webinars"]
    collection = db["webinar-details"]
    team = {}
    for x in collection.find({}, { "_id": { "$slice": -1 } }):
        team = x

    #print("Connection closed") """collection.find({"name" :{ "$eq" : "" }}, { "_id":0}):"""
    return (team)
    client.close()
