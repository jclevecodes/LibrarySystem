from UserDatabase import UserDatabase
from Book import Book
user = UserDatabase()
# book = Book()

class UserService:
    
    def userRegistration(self):
        userName = input(f"Enter your name: ")
        userID = input(f"Enter your ID number: ")

        user.addUserToDatabase(userName, userID, True)
        
        print("----------------------------------------------------------------------------------")
        print(f"{userName} with ID #{userID} has been registered within our library system!")
        print("----------------------------------------------------------------------------------\n")

    def loadBooks(self):
        user.personLoad(True)

    def userVerification(self, id):
    
        # id = input("Enter ID # of user: ")
        if id in user.idDict:
            print(f"{id} is registered with this user\n {user.idDict[id]}")
            return True, user.idDict[id]
        else: 
            print("User does not exist in database")
            return False, None


    def borrowBook(self, userName, userID, bookTitle):
        verified = userServ.userVerification(userID)
        if (verified[0] == True):
            print("Book already borrowed by a user!")
        else:
            user.addBookTo

if __name__ == "__main__":
    userServ = UserService()
    userServ.borrowBook("Joshua Cleveland", "23023", "test")
            

    

    

