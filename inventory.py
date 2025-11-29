import json
from pathlib import Path
from book import Book 

class LibraryInventory:
    def __init__(self, file_path='books.json'):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def load_books(self):
        if self.file_path.exists():
            with open(self.file_path, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(**data) for data in books_data]
        else:
            self.books = []

    def save_books(self): 
        with open(self.file_path, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        return [book.get_book_info() for book in self.books]
    def update_book_status(self, isbn, new_status):
        book = self.find_book(isbn)
        if book:
            if new_status == "available":
                book.return_book()
            elif new_status == "borrowed":
                book.borrow_book()
            elif new_status == "reserved":
                book.reserve_book()
            self.save_books()
            return True
        return False
