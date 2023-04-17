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
                if titleSearch in data.titleDict:
                    print(f"{data.titleDict[titleSearch]}")
            case "2":
                authorSearch = input("Enter book author: ")
                if authorSearch in data.authorDict:
                    print(f"{data.authorDict[authorSearch]}")
            case "3":
                isbnSearch = input("Enter book ISBN: ")
                if isbnSearch in data.isbnDict:
                    print(f"{data.isbnDict[isbnSearch]}")

    def getAvailableBookId(self):
        list = data.checkoutCopies
        print(list)
        

if __name__ == "__main__":
    book = BookService()
    book.getAvailableBookId()