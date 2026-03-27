# Q2: Create a Library Management System
# a) Design classes for Book, Member, and Library
# b) Implement methods for adding books, lending books, returning books, displaying books
# c) Create a menu-driven interface

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        book = Book(book_id, title)
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(book.book_id, "-", book.title, "-", status)

    def lend_book(self):
        book_id = int(input("Enter Book ID to lend: "))
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return
        print("Book not found!")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned successfully!")
                return
        print("Book not found!")


# Menu-driven program
lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.display_books()
    elif choice == 3:
        lib.lend_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")