from CSVDatabase import CSVDatabase
from UserDatabase import UserDatabase
data = CSVDatabase()
user = UserDatabase()

class LibManager:

    def userRegistration(self):
            userName = input(f"Enter your name: ")
            userID = input(f"Enter your ID number: ")

            user.addUserToDatabase(userName, userID, True)
            
            print("----------------------------------------------------------------------------------")
            print(f"{userName} with ID #{userID} has been registered within our library system!")
            print("----------------------------------------------------------------------------------\n")

    def addBook(self):
        bookTitle = input("Enter the book Title: ")
        bookAuthor = input("Enter the book Author: ")
        bookISBN = input("Enter the book ISBN number: ")
        
        data.addBookToDatabase(bookTitle, bookAuthor, bookISBN, True)
        print("----------------------------------------------------------------------------------------------")
        print(f"{bookTitle} by {bookAuthor} with ISBN #{bookISBN}has been added to our library!") 
        print("----------------------------------------------------------------------------------------------\n")

    def bookLookup(self):
        searchMethod = input("How would you like to search for book? 1. Title 2. Author 3. ISBN\n")

        match searchMethod:
            case "1":
                titleSearch = input("Enter book title: ")
                data.searchByTitle(titleSearch)
            case "2":
                authorSearch = input("Enter book author: ")
                data.searchByAuthor(authorSearch)
            case "3":
                isbnSearch = input("Enter book ISBN: ")
                data.searchByISBN(isbnSearch)