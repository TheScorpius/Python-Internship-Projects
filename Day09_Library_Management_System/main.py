from library import Library

def main():
    lib = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(book_id, title, author)

        elif choice == "2":
            lib.display_books()

        elif choice == "3":
            book_id = input("Book ID to issue: ")
            lib.issue_book(book_id)

        elif choice == "4":
            book_id = input("Book ID to return: ")
            lib.return_book(book_id)

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()