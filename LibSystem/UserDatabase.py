import csv
from User import User
FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/users.csv'

class UserDatabase:

    nameDict = {}
    idDict = {}

    def __init__(self):

        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                # Grab info from csv file and store info in assigned variables
                name = row[0]
                id = row[1]

                self.addUserToDatabase(name, id)

    def addUserToDatabase(self, name, id, addUser = False):

        # Instantiate book object
        user = User(name, id)

        # Store book inside assigned dictionary
        self.nameDict[name] = user
        self.idDict[id] = user

        if (addUser == True):
            with open(FILE_PATH, mode='a', newline="\n") as file:
                writer = csv.writer(file)

                writer.writerow([name, id])