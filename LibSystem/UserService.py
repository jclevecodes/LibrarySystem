from UserDatabase import UserDatabase
user = UserDatabase()

class UserService:

    def userRegistration(self):
        userName = input(f"Enter your name: ")
        userID = input(f"Enter your ID number: ")

        user.addUserToDatabase(userName, userID, True)
        
        print("----------------------------------------------------------------------------------")
        print(f"{userName} with ID #{userID} has been registered within our library system!")
        print("----------------------------------------------------------------------------------\n")
        
    def userVerification(self):
        id = input("Enter ID # of user: ")
        if id in user.idDict:
            print(f"{id} is registered with this user\n {user.idDict[id]}")

    

    

