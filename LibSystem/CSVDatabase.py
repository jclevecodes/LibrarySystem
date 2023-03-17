import csv
from Book import Book 

FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/books.csv'

class CSVDatabase:

    titleDict = {}
    authorDict = {}
    isbnDict = {}

    def __init__(self):
        # requestData = True
        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                # Grab info from csv file and store info in assigned variables
                title = row[0]
                author = row[1]
                isbn = row[2]

                self.addBookToDatabase(title, author, isbn)

    '''
        
    '''
    def addBookToDatabase(self, title, author, isbn, addBook = False):

        # Instantiate book object
        book = Book(author, title, isbn)

        # Store book inside assigned dictionary
        self.titleDict[title] = book
        self.authorDict[author] = book
        self.isbnDict[isbn] = book

        if (addBook == True):
            with open(FILE_PATH, mode='a', newline="\n") as file:
                writer = csv.writer(file)

                writer.writerow([title, author, isbn])

        


    def searchByTitle(self, searchedTitle):
        searchResult = input("Enter book title\n")
        seen_keys = set()
        for key in self.titleDict.items():
            if searchResult in self.titleDict.keys():
                print("DOUBLE TITLES")

        if searchedTitle in self.titleDict:
            print(f"{self.titleDict[searchedTitle]}")
        else:
            print("Book not located in system.")

    def searchByAuthor(self, searchedAuthor):
        if searchedAuthor in self.authorDict:
            print(f"{self.authorDict[searchedAuthor]}")
        else:
            print("Book not located in system.")

    def searchByISBN(self, searchedISBN):
        if searchedISBN in self.authorDict:
            print(f"{self.authorDict[searchedISBN]}")
        else:
            print("Book not located in system/")


if __name__ == "__main__":
    data = CSVDatabase()
    # data.addBookToDatabase("asds", "asdasd", "124235345", True)

    searching = input("Search library using 1. Title 2. Author 3. ISBN\n")


    if (searching == "1"):
        
        data.searchByTitle(searchResult)
    elif (searching == "2"):
        searchResult = input("Enter book author\n")
        data.searchByAuthor(searchResult)
    elif (searching == "3"):
        searchResult = input("Enter book ISBN\n")
        data.searchByISBN(searchResult)