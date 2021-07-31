from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") #host uri
db = client.mymongodb    #Select the database
todos = db.todo #Select the collection name

def insertRecord(x, y):
    print('insertRecord')
    mydict = {"name": x, "address": y}
    x = todos.insert_one(mydict)

def listRecords():
    x = todos.find({})
    items = []
    print (x)
    for obj in x:
        print(obj)
        items.append(obj)
    return items

if __name__ == "__main__":
    listRecords()



