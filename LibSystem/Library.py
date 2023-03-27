from LibManager import LibManager
manage = LibManager() 

class Library:
    
    def menu(self):
        searching = True

        print("Choose menu item")
        while (searching == True):
            choice = input("| 1. Registration | 2. Add Book | 3. Lookup Book | 4. Check-in | 5. Check-out | 6. Finish library |\n")

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
                    searching = False
                case _:
                    print("Invalid Option. Try again!")

if __name__ == "__main__":
    lib = Library()
    lib.menu()