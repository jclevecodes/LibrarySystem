import csv
from User import User
FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/users.csv'


class UserDatabase:

    def __init__(self):
        self.nameDict = {}
        self.idDict = {}
        
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
            if name in self.nameDict:
                print(f"{name} is currently registered already")
            with open(FILE_PATH, mode='a', newline="\n") as file:
                writer = csv.writer(file)

                writer.writerow([name, id])