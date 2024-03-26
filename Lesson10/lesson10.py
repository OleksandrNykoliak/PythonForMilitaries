from datetime import datetime

class Book:
    def __init__(self, title, author, publisher='Не вказали видавництво'):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:  # Якщо книга вже взята
            print(f'Книгу {self.title} вже взяли почитати')
            return False      # Повертаємо False, щоб показати, що книгу не можна взяти
        else:
            print(f'Ви успішно взяли почитати {self.title} {datetime.now().__format__("%Y-%m-%d %H:%M:%S")}')
            self.is_borrowed = True    # Позначаємо, що книгу взяли
            return True                # Повертаємо True, щоб показати, що книгу можна взяти

    def return_book(self):
        if self.is_borrowed:
            print(f'Ви успішно повернули книгу {self.title} {datetime.now().__format__("%Y-%m-%d %H:%M:%S")}')
            self.is_borrowed = False
        else:
            print(f'Книга {self.title} знаходиться в бібліотеці {datetime.now().__format__("%Y-%m-%d %H:%M:%S")}')
            
    def who_is_publisher(self):
        return f'Книгу {self.title} видали: {self.publisher}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книгу {book.title} додано до бібліотеки {datetime.now().__format__("%Y-%m-%d %H:%M:%S")}')

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                return book.borrow_book()
        print(f'Книгу {title} не знайдено або вже взяли')
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f'Книгу {title} не знайдено')

    def list_books(self):
        print(f'Наш бібліотечний фонд налічує {len(self.books)} книги')
        
        for book in self.books:
            if not book.is_borrowed:
                print(f'{book.title} - в бібліотеці')
            elif book.is_borrowed:
                print(f'{book.title} - взята')

    def __str__(self) -> str:
        for book in self.books:
            if not book.is_borrowed and len(self.books) > 1:
                return f'У бібліотеці {len(self.books)} книги:\n{[book.title for book in self.books]}'
            elif not book.is_borrowed and len(self.books) == 1:
                return f'У бібліотеці {len(self.books)} книга:\n{[book.title for book in self.books]}'
        
my_library = Library()

book1 = Book('Harry Potter', 'J.K. Rowling')
book2 = Book('The Lord of the Rings', 'J.R.R. Tolkien')

my_library.add_book(book1) # Книгу Harry Potter додано до бібліотеки
my_library.add_book(book2) # Ви успішно взяли почитати The Lord of the Rings

book2.borrow_book()  # Ви успішно взяли почитати The Lord of the Rings

my_library.list_books()

book2.return_book()  # Ви успішно повернули книгу The Lord of the Rings

my_library.list_books()

print(my_library)

print(book1.who_is_publisher())