from CSVDatabase import CSVDatabase
data = CSVDatabase()

class BookService:
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