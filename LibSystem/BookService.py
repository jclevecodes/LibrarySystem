from CSVDatabase import CSVDatabase
from UserDatabase import UserDatabase
from User import User
from Book import Book

bookData = CSVDatabase()
userData = UserDatabase()

class BookService:
    def addBook(self, book):
        bookData.books.append(book)
        bookData.addBookToDatabase()

    def borrowedDisplay(self):
        print("Books available for checkout:\n")
        bookData.bookLoad()
        for book in bookData.books:
            if not book.borrowed:
                print(book,"\n")
    
    def checkoutBook(self, userName, bookTitle):
        userData.personLoad()
        user = next((u for u in userData.users if u.name == userName), None)
        if (user):
            bookData.bookLoad()
            book = next((b for b in bookData.books if b.title == bookTitle), None)
            if (book):
                user.bookBorrow(book)
                # bookData.addBookToDatabase()
                # userData.addUserToDatabase()
            
            else:
                print("Book not found")
        else:
            print("User not found.")
        bookData.addBookToDatabase()

    def returnBook(self, userName, bookTitle):
        # userData.personLoad()
        user = next((u for u in userData.users if u.name == userName), None)
        if (user):
            # bookData.bookLoad()
            book = next((b for b in user.borrowed_books if b.title == bookTitle), None)
            if (book):
                user.returnBook(book)
                # bookData.addBookToDatabase()
                # userData.addUserToDatabase()
            else:
                print("Book not within users books borrowed")
        else:
            print("User not found")

    def loadBooks(self):
        bookData.bookLoad(True)