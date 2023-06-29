# from Database.UserDatabase import UserDatabase
# from Classes.Book import Book
from database import CRUD

crud = CRUD.CRUD('mongodb://localhost:27017', 'library')
# userData = UserDatabase()
# book = Book()

class UserService:
    
    def addUser(self, name, idNum):
        user = {
            "Name": name,
            "IDNumber": idNum
        }

        crud.create("users", user)
        print(f"LOG: New user has been added: {name} - {idNum}")

    def searchBooks(self, option, search):
        match option:
            case "Title":
                # filter = {"Title": {"$regex": contains}}
                # crud.read("books", filter)
                crud.read("books",  {"Title": search})
            case "Author":
                crud.read("books", {"Author": search})
            case "ISBN":
                crud.read("books", {"ISBN": search})

    def searchUsers(self, option, search):
        match option:
            case"Name":
                crud.read("users", {"Name": search})
            case "IDNumber":
                crud.read("users", {"IDNumber": search})

    def displayUsers(self):
        query = None
        crud.read("users", query)

# if __name__ == "__main__":
#     userService = UserService()
#     userService.userVerification(238942)

            

    

    

