import unittest
from Books import Books

class TestBooks(unittest.TestCase):

    books = Books()

    def test_RequestListOfGenre(self):
        self.books.populateGenres()
        request = self.books.requestListOfGenre()
        self.assertEqual(request,"Select 0 for Action 1 for Romance 2 for Thriller enter 3 to exit.")

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
