from BooksDataSource import BooksDataSource

class BooksFromFake(BooksDataSource):

    def getListOfGenres(self):
        return ["Action","Romance"]

    def getBooks(self, genre):
        if genre == "Action":
            booksList = ['The Hunt for Red October,Tom Clancy', 'Killing Floor,Lee Child']
        elif "Romance":
            bookList = ['Pride and Prejudice,Jane Austen', 'Jane Eyre,Charlotte Bronte']
        elif "Thriller":
            bookList = ["The Da' Vinci Code,Dan Brown", 'Dracular,Bram Stoker']

        return booksList
