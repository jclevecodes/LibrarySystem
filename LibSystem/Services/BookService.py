from Database.CSVDatabase import CSVDatabase
from Database.UserDatabase import UserDatabase
from Database.CRUD import CRUD
from Classes.User import User
from Classes.Book import Book

crud = CRUD('mongodb://localhost:27017', 'library')
bookData = CSVDatabase()
userData = UserDatabase()

class BookService:
    def addBook(self, title, author, isbn):
        book = {
            "Title": title,
            "Author": author,
            "ISBN": isbn,
            "Availability": 0,
            "Copies" : 1
        }
        crud.create("books", book)
        print(f"LOG: New book has been added: {title} by {author}")
    
    def checkoutBook(self, userName, bookTitle):
        query = {"Title": bookTitle, "Copies": {"$gt": 0}}
        book = crud.read("books", query)
    
        if book:
            update = {"$inc": {"Copies": -1}}
            crud.update("books", query, update)

            userQuery = {"Name": userName}
            crud.update("users", userQuery, {"$push": {"BorrowedBooks": bookTitle}})
            print("Added Book!")
        else:
            print("Book is not available to checkout.")

    def returnBook(self, userName, bookTitle):
        query = {"Title": bookTitle, "Copies": {"$gt": -1}}
        book = crud.read("books", query)
    
        if book:
            update = {"$inc": {"Copies": 1}}
            crud.update("books", query, update)

            userQuery = {"Name": userName}
            crud.update("users", userQuery, {"$pull": {"BorrowedBooks": bookTitle}})
            print("Added Book!")
        else:
            print("Book is not available to checkout.")

    def displayAvailableBooks(self):
        query = {'Copies': {"$gt": 0}}
        crud.read("books", query)
    
    def displayBooks(self):
        query = None
        crud.read("books", query)

# if __name__ == "__main__":
#     bs = BookService()
#     bs.checkoutBook("john", "One Hundred Years of Solitude")