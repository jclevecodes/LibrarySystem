from LibManager import LibManager
manage = LibManager() 

class Library:
    
    def menu(self):
        searching = True

        print("Choose menu item")
        while (searching == True):
            choice = input("| 1. Registration | 2. Add Book | 3. Lookup Book | 4. Check-in | 5. Check-out | 6. Load Books | 7. Finish library |\n")

            match choice:
                case "1":
                    manage.user.userRegistration()
                case "2":
                    manage.book.addBook()
                case "3":
                    manage.book.bookLookup()
                case "4":
                    manage.user.userVerification()
                case "5":
                    manage.user.userVerification()
                case "6":
                    manage.book.loadBooks()
                case "7":
                    searching = False
                case _:
                    print("Invalid Option. Try again!")
                    print("test")

if __name__ == "__main__":
    lib = Library()
    lib.menu()