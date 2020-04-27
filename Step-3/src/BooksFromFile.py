import os
from BooksDataSource import BooksDataSource

class BooksFromFile(BooksDataSource):

    resourcePath = "C:/Users/Derek/Documents/GitHub/BookShop/resource/"

    def getListOfGenres(self):
        return os.listdir(self.resourcePath)

    def getBooks(self, genre):
        bookFile = open(self.resourcePath + genre + ".txt","r")
        bookData = bookFile.read().splitlines()
        bookFile.close()
        return bookData
