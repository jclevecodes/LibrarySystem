class Book:
    def __init__(self, bookAuthor, bookTitle, bookISBN):
        self.author = bookAuthor    
        self.title = bookTitle
        self.isbn = bookISBN

    def __str__(self):
        return f"Author: {self.author} Title: {self.title} ISBN: {self.isbn}"

    def getAuthor(self):
        return(self.author)
    
    def getTitle(self):
        return(self.title)
    
    def getISBN(self):
        return(self.isbn)
    
