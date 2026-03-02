# ---------------------------------------------------------
# Project: Library Management System (OOP)
# Author: Alvee Rahman (Final Year CSE Student)
# Goal: Implementing Object-Oriented Programming (OOP)
# ---------------------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title} | Author: {self.author} | Status: {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"✔️ Added: {title} to the library.")

    def show_books(self):
        if not self.books:
            print("\n[Alert] Library is empty.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"✅ You borrowed '{book.title}'.")
                else:
                    print(f"❌ '{book.title}' is already borrowed.")
                return
        print("❌ Book not found!")

def main():
    my_library = Library()
    
    # Adding some default books for practice
    my_library.add_book("Python Programming", "Guido van Rossum")
    my_library.add_book("Clean Code", "Robert C. Martin")

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow a Book")
        print("4. Exit")
        
        choice = input("Choice (1-4): ")
        
        if choice == '1':
            t = input("Title: ")
            a = input("Author: ")
            my_library.add_book(t, a)
        elif choice == '2':
            my_library.show_books()
        elif choice == '3':
            t = input("Enter book title to borrow: ")
            my_library.borrow_book(t)
        elif choice == '4':
            print("Exiting... Happy Reading!")
            break
        else:
            print("Invalid Option!")

if __name__ == "__main__":
    main()