from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))
        print("Book added successfully")

    def display_books(self):
        if not self.books:
            print("No books in library")
            return
        for book in self.books:
            print(book)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_issued:
                book.is_issued = True
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_issued:
                book.is_issued = False
                print("Book returned")
                return
        print("Invalid book ID")