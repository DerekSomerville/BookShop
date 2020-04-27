import os
from BooksDataSource import BooksDataSource

class BooksFromStub(BooksDataSource):

    def getListOfGenres(self):
        return ["Action","Romance"]

    def getBooks(self, genre):
        return ['The Hunt for Red October,Tom Clancy', 'Killing Floor,Lee Child']
