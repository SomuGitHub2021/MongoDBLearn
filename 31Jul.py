from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") #host uri
db = client.mymongodb    #Select the database
todos = db.todo #Select the collection name

def insertRecord():
    print('insertRecord')
    mydict = {"name": "John", "address": "Highway 37"}
    x = todos.insert_one(mydict)

insertRecord()


