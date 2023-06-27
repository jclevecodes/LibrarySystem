import csv
from CRUD import CRUD
from Classes.User import User
FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/users.csv'

crud = CRUD('localhost', 'mydatabase')


class UserDatabase:

    def __init__(self):
        self.users = []

    def test(self):
        documents = crud.read('users', { 'IDNumber': { '$gt': 2000 } })

        # for doc in documents:
        #     user = User(doc['name'], doc['age'])
        #     self.users.append(user)
        
    # def personLoad(self, loadRequest = False):
    #     with open(FILE_PATH, mode='r') as file:
    #         reader = csv.reader(file)

    #         # Loop over each user row grabbing info from csv file and store info in assigned variables
    #         for row in reader:
    #             name, id = row

    #             user = User(name, id)
    #             self.users.append(user)

    #             if (loadRequest == True):
    #                 print(row)

    # def addUserToDatabase(self):
    #     with open(FILE_PATH, mode='a', newline="\n") as file:
    #         writer = csv.writer(file)

    #         for user in self.users:
    #             writer.writerow([user.name, user.id])

# if __name__ == "__main__":
#     usersD = UserDatabase()
#     usersD.personLoad(True)
#     print(usersD.users)