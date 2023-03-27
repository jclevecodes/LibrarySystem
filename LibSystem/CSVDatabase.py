import csv
from Book import Book 

FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/books.csv'

class CSVDatabase:

    def __init__(self):
        self.titleDict = {}
        self.authorDict = {}
        self.isbnDict = {}

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
        * Method that allows the addition of book to the database
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


"""
if __name__ == "__main__":
    data = CSVDatabase()

    searching = input("Search library using 1. Title 2. Author 3. ISBN\n")

    if (searching == "1"):
        searchResult = input("Enter book title\n")
        data.searchByTitle(searchResult)
    elif (searching == "2"):
        searchResult = input("Enter book author\n")
        data.searchByAuthor(searchResult)
    elif (searching == "3"):
        searchResult = input("Enter book ISBN\n")
        data.searchByISBN(searchResult)
"""