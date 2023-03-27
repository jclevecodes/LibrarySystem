class Book:
    def __init__(self, bookAuthor, bookTitle, bookISBN):
        self.author = bookAuthor    
        self.title = bookTitle
        self.isbn = bookISBN
        self.available = True
        
    def __str__(self):
        if self.available == True:
            availability = "Available"
        else:
            availability = "Unavailable"

        return f"Author: {self.author}\n Title: {self.title}\n ISBN: {self.isbn}\n ({availability})\n"
    
    def checkOut(self):
        self.available = False

    def checkIn(self):
        self.available = True

    def getAuthor(self):
        return(self.author)
    
    def getTitle(self):
        return(self.title)
    
    def getISBN(self):
        return(self.isbn)
    
