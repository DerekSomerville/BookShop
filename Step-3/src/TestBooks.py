import unittest
from Books import Books
from BooksFromStub import BooksFromStub
from BooksFromFile import BooksFromFile
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
        request = self.books.requestListOfGenre()
        self.assertEqual(request,"Select 0 for Action 1 for Romance 2 for Thriller enter 3 to exit.")

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
