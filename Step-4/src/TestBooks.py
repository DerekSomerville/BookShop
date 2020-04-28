import unittest
from Books import Books
from BooksFromStub import BooksFromStub
from BooksFromFile import BooksFromFile
from BooksFromFake import BooksFromFake
from unittest.mock import MagicMock

class TestBooks(unittest.TestCase):

    books = Books()

    def test_RequestListOfGenre(self):
        loadFromFile = BooksFromFile()
        self.books.setLoadBookFile(loadFromFile)
        self.books.populateGenres()
        request = self.books.requestListOfGenre()
        self.assertEqual(request,"Select 0 for Action 1 for Romance 2 for Thriller enter 3 to exit.")

    def test_RequestListOfGenreStubb(self):
        loadFromStub = BooksFromStub()
        self.books.setLoadBookFile(loadFromStub)
        self.books.populateGenres()
        request = self.books.requestListOfGenre()
        self.assertEqual(request,"Select 0 for Action 1 for Romance enter 2 to exit.")

    def test_RequestListOfGenreMock(self):
        loadFromFile = BooksFromFile()
        self.books.setLoadBookFile(loadFromFile)
        self.books.populateGenres()
        self.books.loadBookFile.getListOfGenres = MagicMock(return_value=['Action','Thriller'])
        request = self.books.requestListOfGenre()
        self.assertEqual(request,"Select 0 for Action 1 for Romance 2 for Thriller enter 3 to exit.")

    def test_getBooksForGenreFake(self):
        loadFromFake = BooksFromFake()
        self.books.setLoadBookFile(loadFromFake)
        self.books.populateGenres()
        genreBooks = self.books.getBooksForGenre("Action")
        self.assertEqual(genreBooks,['The Hunt for Red October,Tom Clancy', 'Killing Floor,Lee Child'])

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
