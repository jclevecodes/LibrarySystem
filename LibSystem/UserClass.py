class User:
    def __init__(self, userName = "", userID = ""):
        self.name = userName 
        self.id = userID

    def __str__(self):
        return f"Name: {self.name} ID: {self.id}"
    
    def getName(self):
        return (self.name)
    
    def getID(self):
        return (self.id)






