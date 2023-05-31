class Book:
    def __init__(self, bookAuthor, bookTitle, bookISBN, borrowed = False):
        self.author = bookAuthor    
        self.title = bookTitle
        self.isbn = bookISBN
        self.borrowed = borrowed
        
    def __str__(self):
        bookStatus = "Borrowed" if self.borrowed else "Available"
        return f"Author: {self.author}\n Title: {self.title}\n Isbn: {self.isbn} - {bookStatus}"
    
    # def checkOut(self):
    #     self.available = False

    # def checkIn(self):
    #     self.available = True

    def getAuthor(self):
        return(self.author)
    
    def getTitle(self):
        return(self.title)
    
    def getISBN(self):
        return(self.isbn)
    
    

    
