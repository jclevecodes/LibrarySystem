from pymongo import MongoClient
from mongoengine import *
import json

connect(db="library", host="localhost", port=27017)

class CRUD():
    def __init__(self, connectLink, dbName):
        self.client = MongoClient(connectLink)
        self.db = self.client[dbName]
        # collection = db["users"]

    def create(self, collectionName, document):
        collection = self.db[collectionName]
        collection.insert_one(document)

    def read(self, collectionName, filter=None):
        # filter = {"author": "/^Rob/"}
        # filter = {"author": {"$regex": "^Rob"}}
        collection = self.db[collectionName]
        documents = collection.find(filter)
        for doc in documents:
            print(doc)

    def update(self, collectionName, filter, update):
        collection = self.db[collectionName]
        result = collection.update_one(filter, update)

    def delete(self, collectionName, filter):
        collection = self.db[collectionName]
        result = collection.delete_one(filter)

class Users(Document):
    name = StringField(unique=True)
    idNum = IntField(unique=True)

    def json(self):
        user_dict = {
            "name": self.name,
            "idNum": self.idNum
        }

        return json.dumps(user_dict)

class Books():
    # title = StringField()
    # author = StringField()
    # isbn = StringField(unique=True)
    # availability = BooleanField(default=True)
    # copies = IntField(default=1)

    def __init__(self, title, author, isbn, availability, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        self.copies = copies

    def json(self):
        print()
        # book_dict = {
        #     "title": self.title,
        #     "author": self.author,
        #     "isbn": self.isbn,
        #     "availability": self.availability,
        #     "copies": self.copies
        # }
        
        # return json.dumps(self)

if __name__ == "__main__":
    db = CRUD('mongodb://localhost:27017', 'library')
    books = Books(
        title="Rich Dads Poor Dad",
        author="Robert Kiyosaki",
        isbn="9770446677425",
        availability=True,
        copies=1
    )

    # jsonstr = json.dumps(books)
    bookDict = books.__dict__

    # uj = Users()
    # test = uj.json()
    # print(test)
    # db.create("books", bookDict)
    filter = {"author": {"$regex": "^Rob"}}
    db.read("books", filter)

    # db.read("users", {"idNum": {"$lt": 2356}})

    # users = Users(
    #     name="John",
    #     idNum=2465
    # ).save()

    

    print("Done")
