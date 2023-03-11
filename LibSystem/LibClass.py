from CSVDatabase import CSVDatabase

class Lib:
    # libdict = {'ISBN': '1234', 'author': 'Josh C.'}
    libdict = {}

    def addBook(self):
        bookTitle = ''
        bookAuthor = ''
        bookISBN = ''
        
        bookTitle = input("Enter the book Title: ")
        bookAuthor = input("Enter the book Author: ")
        bookISBN = input("Enter the book ISBN number: ")
        
        data = CSVDatabase()
        data.addBookToDatabase(bookTitle, bookAuthor, bookISBN, True)

    def bookLookup(self):
        bookISBN = input("Enter ISBN # to locate book")
        print(bookISBN)
        if bookISBN in self.libdict:
            print(self.libdict[bookISBN])
    
    def menu(self):
        print("BLAHHHHHH")
        print('test')
        searching = True
        # print("Inside of menu()")
        choice = ''

        print("Choose menu item")
        while (searching == True):
            choice = input("1. Add Book 2. Lookup Book 3. Check-in 4. Check-out 5. Finish library\n")

            match choice:
                case "1":
                    lib.addBook()
                case "2":
                    lib.bookLookup()
                case "3":
                    print()
                case "4":
                    print()
                case "5":
                    searching = False

if __name__ == "__main__":
    # data = CSVDatabase()
    # data.addBookToDatabase()
    lib = Lib()
    lib.menu()