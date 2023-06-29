from database import CRUD
crud = CRUD.CRUD('mongodb://localhost:27017', 'library')

class Book:
    def __init__(self, bookTitle, bookAuthor, bookISBN, copies):  
        self.title = bookTitle
        self.author = bookAuthor  
        self.isbn = bookISBN
        self.copies = copies
    
    def isBorrowed(self):
        books = crud.read("books", {"copies": {"$lt": 1}})


    # def setBorrowed(self):
    #     if self.borrowed:
    #         self.copies -= 1
    #     else:
    #         self.copies += 1

    def __str__(self):
        # bookStatus = "BORROWED" if self.borrowed else "AVAILABLE"
        return f"Title: {self.title}\n Author: {self.author}\n  Isbn: {self.isbn}\n Copies: {self.copies}\n"
    

    # def getAuthor(self):
    #     return(self.author)
    
    # def getTitle(self):
    #     return(self.title)
    
    # def getISBN(self):
    #     return(self.isbn)

# if __name__ == "__main__":
#     book = Book("tesing", "testing", "tesing", 20)
#     book.isBorrowed()
    
    

    
