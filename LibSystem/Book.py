class Book:
    def __init__(self, bookTitle, bookAuthor, bookISBN, borrowed = False):  
        self.title = bookTitle
        self.author = bookAuthor  
        self.isbn = bookISBN
        self.borrowed = borrowed
        
    def __str__(self):
        bookStatus = "Borrowed" if self.borrowed else "Available"
        return f"Title: {self.title}\n Author: {self.author}\n  Isbn: {self.isbn} - {bookStatus}"
    

    # def getAuthor(self):
    #     return(self.author)
    
    # def getTitle(self):
    #     return(self.title)
    
    # def getISBN(self):
    #     return(self.isbn)
    
    

    
