import csv
from Book import Book
# book = Book("234", "we", "sdf")

FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/users.csv'


class User:

    def __init__(self, userName, userID):
        self.name = userName
        self.id = userID
        self.borrowed_books = []

    def book_borrow(self, theBook):
        # print("TEST",theBook.borrowed)
        if theBook.borrowed:
            print("Book is already borrowed")
        else:
            theBook.borrowed = True
            self.borrowed_books.append(theBook)
            print(f"{self.name} has borrowed the book: {theBook.title}")
    
    def return_book(self, theBook):
        if theBook in self.borrowed_books:
            theBook.borrowed = False
            self.borrowed_books.remove(theBook)
            print(f"{self.name} has returned the book: {theBook.title}")
        else:
            print("You have not borrowed this book.")
            

    def __str__(self):
        return (f"Name: {self.name}\n ID: {self.id}\n")

    def getName(self):
        return (self.name)
    
    def setName(self, nameOfUser):
        self.name = nameOfUser
    
    def getID(self):
        return (self.id)
    
    def setID(self, idOfUser):
        self.id = idOfUser

if __name__ == "__main__":
    user = User("josh", "2343")
    user.book_borrow("john")
    print("hello world")