from abc import ABC, abstractmethod

class BooksDataSource(ABC):

    @abstractmethod
    def getListOfGenres(self):
        pass

    @abstractmethod
    def getBooks(self):
        pass
