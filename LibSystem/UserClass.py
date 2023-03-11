class User:
    def __init__(self, userName = "", userID = ""):
        self.name = userName 
        self.id = userID


    def getName(self):
        return (self.name)
    
    def setName(self, userName):
        self.name = userName
    
    def getID(self):
        return (self.id)
    
    def setID(self, userID):
        self.id = userID

#creating an object of the class
random = User('John Doe', '243340')

#print the call of the instance method using the object
# print("------------")
# print(random.getName())
# print(random.getID())







