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
            
            # Looping over each book row
            for row in reader:
                checkoutCopies = []
                # print(type(row))
                # print(row)
                # Grab info from csv file and store info in assigned variables
                title = row[0]
                author = row[1]
                isbn = row[2]

                
                for i in range(3, len(row)):
                    checkoutCopies.append(row[i])

                
                self.addBookToDatabase(title, author, isbn, checkoutCopies)
            
                # print(checkoutCopies)
                checkoutCopies = []


    '''
        * Method that allows the addition of book to the database
    '''
    def addBookToDatabase(self, title, author, isbn, addBook = False):
        # Instantiate book object
        book = Book(author, title, isbn)
        # print(book)
        # Store book inside assigned dictionary
        self.titleDict[title] = book
        self.authorDict[author] = book
        self.isbnDict[isbn] = book
        
        
        if (addBook == True):
            if title in self.titleDict:
                print(f"{title} is currently in the library already.")
            else:
                with open(FILE_PATH, mode='a', newline="\n") as file:
                    writer = csv.writer(file)

                    writer.writerow([title, author, isbn])


if __name__ == "__main__":
    data = CSVDatabase()
    