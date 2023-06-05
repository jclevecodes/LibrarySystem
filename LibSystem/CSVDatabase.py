import csv
from Book import Book 
FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/books.csv'

class CSVDatabase:

    def __init__(self):
        self.books = []

    def bookLoad(self, loadRequest = False):
        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            
            # Loop over each book row grabbing info from csv file and store info in assigned variables
            for row in reader:
                title, author, isbn, borrowed = row

                book = Book(title, author, isbn, bool(int(borrowed)))
                self.books.append(book)

                if (loadRequest == True):
                    print(row)

    def addBookToDatabase(self):
        with open(FILE_PATH, mode='w', newline="\n") as file:
            writer = csv.writer(file)

            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn, int(book.borrowed)])

# if __name__ == "__main__":
#     db = CSVDatabase()
#     db.bookLoad(True)
#     print(db.books)