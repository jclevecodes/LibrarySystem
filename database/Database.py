from abc import ABC, abstractmethod
FILE_PATH = '/Users/joshuacleveland/Desktop/LibrarySystem/LibSystem/books.csv'

class Database(ABC):
    @abstractmethod
    def dataLoad(self):
        pass

    @abstractmethod
    def addData(self):
        pass