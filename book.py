#Name-Abhinav Kumar Singh
#Rollno-2501350083
#Course-Btech cse(FSD)
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._status = status

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self._status}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self._status
        }
    
    def is_available(self):
        return self._status == "available"
    def borrow_book(self):
        if self.is_available():
            self._status = "borrowed"
            return True
        return False
    def return_book(self):
        self._status = "available"
    def reserve_book(self):
        if self.is_available():
            self._status = "reserved"
            return True
        return False
    def cancel_reservation(self):
        if self._status == "reserved":
            self._status = "available"
            return True
        return False
