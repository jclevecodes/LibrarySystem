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

    def bookLookup(self):
        searchMethod = input("How would you like to search for book? 1. Title 2. Author 3. ISBN\n")

        match searchMethod:
            case "1":
                titleSearch = input("Enter book title: ")
                if titleSearch in bookData.titleDict:
                    print(f"{bookData.titleDict[titleSearch]}")
            case "2":
                authorSearch = input("Enter book author: ")
                if authorSearch in bookData.authorDict:
                    print(f"{bookData.authorDict[authorSearch]}")
            case "3":
                isbnSearch = input("Enter book ISBN: ")
                if isbnSearch in bookData.isbnDict:
                    print(f"{bookData.isbnDict[isbnSearch]}")

    def borrowedDisplay(self, userName, userID):
        print()
    
    def checkoutBook(self, userName, bookTitle):
        userData.personLoad()
        user = next((u for u in userData.users if u.name == userName), None)
        if (user):
            bookData.bookLoad()
            book = next((b for b in bookData.books if b.title == bookTitle), None)
            if (book):
                user.bookBorrow(book)
                bookData.addBookToDatabase()
                userData.addUserToDatabase()
            else:
                print("Book not found")
        else:
            print("User not found.")

    def returnBook(self, userName, bookTitle):
        # userData.personLoad()
        user = next((u for u in userData.users if u.name == userName), None)
        if (user):
            # bookData.bookLoad()
            book = next((b for b in user.borrowed_books if b.title == bookTitle), None)
            if (book):
                user.returnBook(book)
                bookData.addBookToDatabase()
                userData.addUserToDatabase()
            else:
                print("Book not within users books borrowed")
        else:
            print("User not found")

    def loadBooks(self):
        bookData.bookLoad(True)