import pymongo


def getWebinarDetailsFromMongo():
    client = pymongo.MongoClient("127.0.0.1", 27017)
    #print("Connection Successful")
    db = client["Webinars"]
    collection = db["webinar-details"]
    team = {}
    for x in collection.find({}, { "_id": { "$slice": -1 } }):
        team = x

    #print("Connection closed") """collection.find({"Title" :{ "$eq" : title }}, { "_id":0}):"""
    return (team)
    client.close()

def getAiInfoFromMongo(title):
    client = pymongo.MongoClient("127.0.0.1", 27017)
    #print("Connection Successful")
    db = client["ArtificialIntellegence"]
    collection = db["ArtificialIntellegenceCollection"]
    ai = {}
    for x in collection.find({"Title" :{ "$eq" : title }}):
        ai = x

    #print("Connection closed") 
    return (ai)
    client.close()