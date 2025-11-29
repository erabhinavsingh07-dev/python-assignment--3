#NAME :ABHINAV KUMAR SINGH
#ROLL NO.:2501350083
#COURSE:BTECH CSE(FSD)


from inventory import LibraryInventory
from book import Book

def menu():
    print("\nLibrary Inventory System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Find Book")
    print("4. List All Books")
    print("5. Update Book Status")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            inventory.remove_book(isbn)
            print("Book removed successfully.")

        elif choice == '3':
            isbn = input("Enter book ISBN to find: ")
            book = inventory.find_book(isbn)
            if book:
                print(book.get_book_info())
            else:
                print("Book not found.")

        elif choice == '4':
            books = inventory.list_books()
            if books:
                for info in books:
                    print(info)
            else:
                print("No books in inventory.")

        elif choice == '5':
            isbn = input("Enter book ISBN to update status: ")
            new_status = input("Enter new status (available/borrowed/reserved): ").lower()
            if inventory.update_book_status(isbn, new_status):
                print("Book status updated successfully.")
            else:
                print("Failed to update book status. Check ISBN and status.")

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
