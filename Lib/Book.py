class Book:
    def __init__(self, title, author, isbn, borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = borrowed

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} [{self.isbn}] - {status}"