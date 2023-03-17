import csv
FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/users.csv'

class User:

    nameDict = {}
    idDict = {}

    def __init__(self, userName, userID):
        self.name = userName 
        self.id = userID

        with open(FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                # Grab info from csv file and store info in assigned variables
                name = row[0]
                id = row[1]

                self.addUserToDatabase(name, id)

    def __str__(self):
        return f"Name: {self.name} ID: {self.id}"

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

    def getName(self):
        return (self.name)
    
    def setName(self, nameOfUser):
        self.name = nameOfUser
    
    def getID(self):
        return (self.id)
    
    def setID(self, idOfUser):
        self.id = idOfUser






