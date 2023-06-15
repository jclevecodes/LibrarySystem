class Book:
    def __init__(self, bookTitle, bookAuthor, bookISBN, borrowed = False, copies = 1):  
        self.title = bookTitle
        self.author = bookAuthor  
        self.isbn = bookISBN
        self.borrowed = borrowed
        self.copies = copies
    
    def isBorrowed(self):
        return self.copies == 0
    
    def setBorrowed(self):
        if self.borrowed:
            self.copies -= 1
        else:
            self.copies += 1

    def __str__(self):
        bookStatus = "BORROWED" if self.borrowed else "AVAILABLE"
        return f"Title: {self.title}\n Author: {self.author}\n  Isbn: {self.isbn} - ({bookStatus})\n Copies: {self.copies}\n"
    

    # def getAuthor(self):
    #     return(self.author)
    
    # def getTitle(self):
    #     return(self.title)
    
    # def getISBN(self):
    #     return(self.isbn)
    
    

    
