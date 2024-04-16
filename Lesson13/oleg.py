
class DigitalBooks:
    def digitalization(self):
        print("digitalization of books")
            
    def download_book(self):
        print("download_book")
                       
    def read_book(self, book_name):
        print(f"read_book {book_name}")
    
    def search_book(self):
        print("search_book")
        
    def format_book(self):
        print("format_book")
        

class FacadeForReaders:
    def __init__(self):
        self.digital_books = DigitalBooks()

    def read_book(self, some_book):
        print("we are reading the book")
        self.digital_books.read_book(some_book)
        
book1 = DigitalBooks()
book1.read_book('Harry Potter')

access_via_facade = FacadeForReaders()
access_via_facade.read_book('Harry Potter')

