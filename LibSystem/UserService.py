from UserDatabase import UserDatabase
from Book import Book
userData = UserDatabase()
# book = Book()

class UserService:
    
    def userRegistration(self, user):
        userData.users.append(user)
        for i in userData.users:
            print("----",i)
        userData.addUserToDatabase()

    def loadUsers(self):
        userData.personLoad(True)

    def userVerification(self, userName):
        print()
        # userData.personLoad()
        # user = None
        # for u in userData.users:
        #     if u.name == userName:
        #         user = u
        #         break

        # # id = input("Enter ID # of user: ")
        # if id in userData.users:
        #     print(f"{id} is registered")
        # else: 
        #     print("User does not exist in database")




    # def borrowBook(self, userName, userID, bookTitle):
    #     verified = userServ.userVerification(userID)
    #     if (verified[0] == True):
    #         print("Book already borrowed by a user!")
    #     else:
    #         print()

# if __name__ == "__main__":
#     userService = UserService()
#     userService.userVerification(238942)

            

    

    

