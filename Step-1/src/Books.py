from BooksFromFile import BooksFromFile
class Books():

    listOfGenre = []
    listOfBooks = {}
    loadBookFile = BooksFromFile()

    def getPropertyGenres(self):
        listOfGenres = []
        rawListOfGenres = self.loadBookFile.getListOfGenres()
        for genre in rawListOfGenres:
            listOfGenres.append(genre.split(".")[0])
        return listOfGenres

    def populateGenres(self):
        self.listOfGenre = self.getPropertyGenres()

    def setLoadBookFile(self,loadBookFile):
        self.loadBookFile = loadBookFile

    def requestListOfGenre(self):
        request = "Select "
        for counter in range(len(self.listOfGenre)):
            request += str(counter) + " for " + self.listOfGenre[counter] + " "
        request += "enter " + str(len(self.listOfGenre)) + " to exit."
        return request

    def getBookGenreIndex(self):
        return int(input(self.requestListOfGenre()))

    def getBookGenre(self,index):
        return self.listOfGenre[index]

    def getBooksForGenre(self, genre):
        return self.loadBookFile.getBooks(genre)

    def checkIfGenreLoaded(self,genre):
        if genre in self.listOfBooks:
            return True
        else:
            return False

    def storeBooksForGenre(self,genre,listOfBooks):
        print(listOfBooks)
        if not self.checkIfGenreLoaded(genre):
            self.listOfBooks[genre] = listOfBooks

    def getCustomerGenres(self):
        userGenreIndex = 0
        while userGenreIndex < len(self.listOfGenre):
            userGenreIndex = self.getBookGenreIndex()
            if userGenreIndex < len(self.listOfGenre):
                userGenre = self.getBookGenre(userGenreIndex)
                if self.checkIfGenreLoaded(userGenre):
                    print("Please try again, the " + userGenre + " has already been selected")
                else:
                    self.storeBooksForGenre(userGenre,self.getBooksForGenre(userGenre))

    def displayAllBooks(self):
        for genre in self.listOfBooks:
            print("Genre: " + genre)
            self.displayGenreBooks(genre)


    def displayGenreBooks(self,genre):
        for bookRow in self.listOfBooks[genre]:
            book = bookRow.split(",")
            print("Title: " + book[0] + " Author: " + book[1])

    def openShop(self):
        self.populateGenres()
        self.getCustomerGenres()
        self.displayAllBooks()

def main():
    books = Books()
    books.openShop()

if __name__ == '__main__':
    main()
