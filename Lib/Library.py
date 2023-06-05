import csv
from person import Person
from Book import Book

class Library:
    def __init__(self):
        self.books = []
        self.people = []

    def load_books(self):
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                title, author, isbn, borrowed = row
                book = Book(title, author, isbn, borrowed=bool(int(borrowed)))
                self.books.append(book)

    def load_people(self):
        with open('people.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, id_number = row
                person = Person(name, id_number)
                self.people.append(person)

    def save_books(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn, int(book.borrowed)])

    def save_people(self):
        with open('people.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for person in self.people:
                writer.writerow([person.name, person.id_number])

    def display_books(self):
        for book in self.books:
            print(book)

    def display_people(self):
        for person in self.people:
            print(person)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def add_person(self, person):
        self.people.append(person)
        self.save_people()

    def checkout_book(self, person_name, book_title):
        person = next((p for p in self.people if p.name == person_name), None)
        print("---------------------", person)
        if person:
            book = next((b for b in self.books if b.title == book_title), None)
            if book:
                person.borrow_book(book)
                self.save_books()
                self.save_people()
            else:
                print("Book not found.")
        else:
            print("Person not found.")

    def return_book(self, person_name, book_title):
        person = next((p for p in self.people if p.name == person_name), None)
        if person:
            book = next((b for b in person.borrowed_books if b.title == book_title), None)
            if book:
                person.return_book(book)
                self.save_books()
                self.save_people()
            else:
                print("Book not found in person's borrowed books.")
        else:
            print("Person not found.")

    def show_menu(self):
        while True:
            print("\nLIBRARY MENU")
            print("1. Display Books")
            print("2. Display People")
            print("3. Add Book")
            print("4. Add Person")
            print("5. Checkout Book")
            print("6. Return Book")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.display_books()
            elif choice == 2:
                self.display_people()
            elif choice == 3:
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                isbn = input("Enter ISBN: ")
                book = Book(title, author, isbn)
                self.add_book(book)
            elif choice == 4:
                name = input("Enter person's name: ")
                id_number = input("Enter person's ID number: ")
                person = Person(name, id_number)
                self.add_person(person)
            elif choice == 5:
                person_name = input("Enter person's name: ")
                book_title = input("Enter book title: ")
                self.checkout_book(person_name, book_title)
            elif choice == 6:
                person_name = input("Enter person's name: ")
                book_title = input("Enter book title: ")
                self.return_book(person_name, book_title)
            elif choice == 7:
                break
            else:
                print("Invalid choice. Please try again.")


# Create an instance of the Library class and run the program

library = Library()
library.load_books()
library.load_people()
library.show_menu()
