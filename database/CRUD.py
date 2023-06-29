import pymongo 
from pymongo import MongoClient
from classes import Book
from classes import User
# from mongoengine import *
# import json

# connect(db="library", host="localhost", port=27017)

class CRUD():
    def __init__(self, host, dbName):
        self.client = MongoClient(host)
        self.db = self.client[dbName]
        # collection = db["users"]

    def create(self, collectionName, document):
        collection = self.db[collectionName]
        collection.insert_one(document)

    def read(self, collectionName, filter):
        obj = None
        collection = self.db[collectionName]
        documents = collection.find(filter)
        found = list(documents)

        if len(found) == 0:
            print('No documents found for the given query.')
        else:
            if collectionName == "books":
                # print(len(found))
                for doc in found:
                
                    # print(doc["Title"])
                    # print(doc["Author"])
                    # print(doc["ISBN"])
                    # print(doc["Copies"])
                    # print(doc)
                    obj = Book(doc['Title'], doc['Author'], doc['ISBN'], doc['Copies']) 
                    print(obj)
            elif collectionName == "users":
                for doc in found:
                    obj = User(doc["Name"], doc['IDNumber'], doc["BorrowedBooks"])
                    # print(doc)
        print(obj)
        return obj
        

    def update(self, collectionName, filter, update):
        collection = self.db[collectionName]
        result = collection.update_one(filter, update)

    def delete(self, collectionName, filter):
        collection = self.db[collectionName]
        result = collection.delete_one(filter)


if __name__ == "__main__":
    db = CRUD('mongodb://localhost:27017', 'library')
#     query = {'title': "One Hundred Years of Solitude"}
#     test = db.read("books", query)
    
#     books = Books(
#         title="Rich Dads Poor Dad",
#         author="Robert Kiyosaki",
#         isbn="9770446677425",
#         availability=True,
#         copies=1
#     )

#     bookDict = books.__dict__

    # db.create("books", {"name": "John"})

    # filter = {"author": {"$regex": "^Rob"}}
    # db.read("books", filter)

    result = db.read("books", {"Title": "1984"})
    print("Blah")
    # print(doc.filter)
    print(result)
    
#     print("Done")
