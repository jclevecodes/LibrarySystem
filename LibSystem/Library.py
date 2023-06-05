# from LibManager import LibManager
# manage = LibManager()
from UserService import UserService
from BookService import BookService
userServ = UserService()
bookServ = BookService()

from User import User
from Book import Book

class Library:
    
    def menu(self):
        searching = True

        print("\n---------------------------------------------------------CHOOSE MENU ITEM--------------------------------------------------------")
        while (searching == True):
            choice = input("| 1. Register User | 2. Add Book | 3. Checkout Book | 4. Return Book | 5. Display Books | 6. Display People | 7. Finish library |\n")

            match choice:
                case "1":
                    userName = input(f"Enter your name: ")
                    userID = input(f"Enter your ID number: ")
                    print("----------------------------------------------------------------------------------")
                    print(f"{userName} with ID #{userID} has been registered within our library system!")
                    print("----------------------------------------------------------------------------------\n")
                    user = User(userName, userID)
                    userServ.userRegistration(user)

                case "2":
                    bookTitle = input("Enter the book Title: ")
                    bookAuthor = input("Enter the book Author: ")
                    bookISBN = input("Enter the book ISBN number: ")
                    print("----------------------------------------------------------------------------------------------")
                    print(f"{bookTitle} by {bookAuthor} with ISBN #{bookISBN}has been added to our library!") 
                    print("----------------------------------------------------------------------------------------------\n")
                    book = Book(bookTitle, bookAuthor, bookISBN)
                    bookServ.addBook(book)

                case "3":
                    userName = input(f"Enter your name: ")
                    bookTitle = input(f"Enter title of book: ")
                    bookServ.checkoutBook(userName, bookTitle)

                case "4":
                    userName = input(f"Enter your name: ")
                    bookTitle = input(f"Enter title of book: ")
                    bookServ.returnBook(userName, bookTitle)

                case "5":
                    print("\n")
                    bookServ.loadBooks()
                    print("\n")

                case "6":
                    print("\n")
                    userServ.loadUsers()
                    print("\n")
                    

                case "7":
                    searching = False

                case _:
                    print("Invalid Option. Try again!")
                    print("test")

if __name__ == "__main__":
    lib = Library()
    lib.menu()