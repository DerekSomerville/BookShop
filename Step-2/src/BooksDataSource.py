from abc import ABC, abstractmethod

class BooksDataSource(ABC):

    @abstractmethod
    def getBooks(self):
        pass
