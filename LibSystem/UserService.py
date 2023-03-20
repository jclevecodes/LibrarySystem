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