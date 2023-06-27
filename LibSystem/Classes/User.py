import csv
from Book import Book
from CSVDatabase import CSVDatabase

# book = Book("234", "we", "sdf")

FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/users.csv'


class User:

    def __init__(self, userName, userID, borrowedBooks):
        self.name = userName
        self.id = userID
        self.borrowedBooks = borrowedBooks

    # def bookBorrow(self, theBook):
    #     # print("TEST",theBook.borrowed)
    #     if theBook.borrowed:
    #         print("Book is already borrowed")
    #     else:
    #         theBook.borrowed = True
    #         theBook.setBorrowed()
    #         self.borrowed_books.append(theBook)
    #         print(f"{self.name} has borrowed the book: {theBook.title}")
    #         if (theBook.copies != 0):
    #             theBook.borrowed = False
    
    # def returnBook(self, theBook):
    #     if theBook in self.borrowed_books:
    #         theBook.borrowed = False
    #         theBook.setBorrowed()
    #         self.borrowed_books.remove(theBook)
    #         print(f"{self.name} has returned the book: {theBook.title}")
    #     else:
    #         print("You have not borrowed this book.")

    # def bookBorrowDisplay(self):
    #     if (self.borrowed_books):
    #         print(f"Books borrowed by {self.name}")
    #         for books in self.borrowed_books:
    #             print(books)

    def __str__(self):
        return (f"Name: {self.name}\n ID: {self.id}\n Borrowed books: {self.borrowedBooks}")

    # def getName(self):
    #     return (self.name)
    
    # def setName(self, nameOfUser):
    #     self.name = nameOfUser
    
    # def getID(self):
    #     return (self.id)
    
    # def setID(self, idOfUser):
    #     self.id = idOfUser
