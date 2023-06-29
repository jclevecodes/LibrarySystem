# # from LibManager import LibManager
# # manage = LibManager()
# # from Services.UserService import UserService
# # from Services.BookService import BookService
# # userServ = UserService()
# # bookServ = BookService()

# # from Classes.User import User
# # from Classes.Book import Book

# class Library:
    
#     def menu(self):
#         searching = True

#         print("\n---------------------------------------------------------CHOOSE MENU ITEM--------------------------------------------------------")
#         while (searching == True):
#             choice = input("| 1. Search Database | 2. Register User | 3. Add Book | 4. Checkout Book | 5. Return Book | 6. Display All Books | 7. Display Available Books | 8. Display People | 9. Finish library |\n")

#             match choice:
#                 case "1": 
#                     searchTerm = input('Would you like to search users or books: ')
#                     match searchTerm:
#                         case "users":
#                             userSearch = input("What would you like to search by: \'Name\' or \'IDNumber\' ")
#                             match userSearch:
#                                 case "Name":
#                                     nameSearch = input("What user are you looking for?: ")
#                                     userServ.searchUsers(userSearch, nameSearch)
#                                 case "IDNumber":
#                                     nameSearch = input("What user are you looking for?: ")
#                                     userServ.searchUsers(userSearch, nameSearch)
#                         case "books":
#                             userSearch = input("What would you like to search by: \'Title\', \'Author\', or \'ISBN\'")
#                             match userSearch:
#                                 case "Title":
#                                     titleSearch = input("What is the title of the book? ")
#                                     userServ.searchBooks(userSearch, titleSearch)
#                                 case "Author":
#                                     authorSearch = input("What is the title of the book? ")
#                                     userServ.searchBooks(userSearch, authorSearch)
#                                 case "ISBN":
#                                     isbnSearch = input("What is the title of the book? ")
#                                     userServ.searchBooks(userSearch, isbnSearch)
#                                     isbnSearch = input("What is the input device that you are attempting to use")

#                 case "2":
#                     userName = input("Enter your name: ")
#                     userName = input("Enter the name of eac user")
#                     userID = input("Enter your ID number: ")
#                     print("----------------------------------------------------------------------------------")
#                     print(f"{userName} with ID #{userID} has been registered within our library system!")
#                     print("----------------------------------------------------------------------------------\n")
#                     userServ.addUser(userName, userID)

#                 case "3":
#                     bookTitle = input("Enter the book Title: ")
#                     bookAuthor = input("Enter the book Author: ")
#                     bookISBN = input("Enter the book ISBN number: ")
#                     print("----------------------------------------------------------------------------------------------")
#                     print(f"{bookTitle} by {bookAuthor} with ISBN #{bookISBN}has been added to our library!") 
#                     print("----------------------------------------------------------------------------------------------\n")
#                     bookServ.addBook(bookTitle, bookAuthor, bookISBN)

#                 case "4":
#                     userName = input("Enter your name: ")
#                     bookTitle = input("Enter title of book: ")
#                     bookServ.checkoutBook(userName, bookTitle)

#                 case "5":
#                     userName = input("Enter your name: ")
#                     bookTitle = input("Enter title of book: ")
#                     bookServ.returnBook(userName, bookTitle)

#                 case "6":
#                     print("\n")
#                     bookServ.displayBooks()
#                     print("\n")

#                 case "7":

#                     print("\n")
#                     bookServ.displayAvailableBooks()
#                     print("\n")

#                 case "8":
#                     print("\n")
#                     userServ.displayUsers()
#                     print("\n")
                
#                 case "9":
#                     searching = False

#                 case _:
#                     print("Invalid Option. Try again!")
#                     print("test")

# if __name__ == "__main__":
#     lib = Library()
#     lib.menu()

