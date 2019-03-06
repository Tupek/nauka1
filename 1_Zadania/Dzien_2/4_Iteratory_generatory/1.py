class Book(object):

    @classmethod
    def silmarillion(cls):
        b = cls()
        b.name = "Silmarillion"
        b.author = "J. R. R. Tolkien"
        b.price = 42.50
        return b
    
book = Book.silmarillion()
book.print_book_info()