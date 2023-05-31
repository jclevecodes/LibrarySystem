import csv
from Book import Book 

FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/books.csv'

class CSVDatabase:

    def __init__(self):
        # self.titleDict = {}
        # self.authorDict = {}
        # self.isbnDict = {}
        self.books = []
        self.users = []

    def bookLoad(self, loadRequest = False):
        # requestData = True
        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            
            # Looping over each book row
            for row in reader:
                title, author, isbn, borrowed = row
                book = Book(title, author, isbn, borrowed=bool(int(borrowed)))
                self.books.append(book)
                # title = row[0]
                # author = row[1]
                # isbn = row[2]

                
                self.addBookToDatabase(title, author, isbn)

                if (loadRequest == True):
                    print(row)
                # print(checkoutCopies)
                # checkoutCopies = []
        


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
            # if title in self.titleDict:
            #     print(f"{title} is currently in the library already.")
            # else:
            with open(FILE_PATH, mode='a', newline="\n") as file:
                writer = csv.writer(file)

                writer.writerow([title, author, isbn])


if __name__ == "__main__":
    data = CSVDatabase()
    