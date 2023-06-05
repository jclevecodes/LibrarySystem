from Book import Book

class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrowed:
            print("Sorry, the book is already borrowed.")
        else:
            book.borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed the book: {book.title}")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print("You have not borrowed this book.")

    def __str__(self):
        return f"{self.name} (ID: {self.id_number})"
    
