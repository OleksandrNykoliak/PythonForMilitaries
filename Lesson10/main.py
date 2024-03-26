from lesson10 import book2, my_library

def check_if_book_exists(book):
    for b in my_library.books:
        if b.title == book.title:
            return 'Книгу знайдено'
    return 'Книгу не знайдено'


print(check_if_book_exists(book2))
