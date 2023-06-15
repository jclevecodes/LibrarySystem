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
                title, author, isbn, borrowed, copies = row

                book = Book(title, author, isbn, bool(int(borrowed)), int(copies))
                self.books.append(book)

                if (loadRequest == True):
                    print(book)

    def addBookToDatabase(self):
        with open(FILE_PATH, mode='a', newline="\n") as file:
            writer = csv.writer(file)

            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn, int(book.borrowed), int(book.copies)])

# if __name__ == "__main__":
#     db = CSVDatabase()
#     db.bookLoad(True)
#     print(db.books)