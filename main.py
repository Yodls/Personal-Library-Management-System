from library import Library  # Imports the Library class from the library module

def print_menu(): # Prints the main menu for the Library Management System
    print("\nLibrary Management System")
    print("1. Add new book")
    print("2. Search books")
    print("3. Update book")
    print("4. Remove book")
    print("5. Display all books")
    print("6. Display books by criteria")
    print("7. Show unique authors")
    print("8. Show unique genres")
    print("9. Exit")

def main(): # Creates an instance of Library to manage the book collection
    lib = Library()
    
    while True:  # repeatedly display the menu and process user input
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1": # Option 1: Add new book to the collection
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            genre = input("Enter book genre: ").strip()
            year_input = input("Enter publication year: ").strip()
            try:
                year = int(year_input)
            except ValueError:
                print("Invalid year. Please enter a valid number.")
                continue
            book = lib.add_book(title, author, genre, year)
            print("Book added:")
            print(book)
            
        elif choice == "2": # Option 2: Search for books by title, author, or genre
            field = input("Search by (title/author/genre): ").strip().lower()
            if field not in ["title", "author", "genre"]:
                print("Invalid search field. Defaulting to title.")
                field = "title"
            query = input(f"Enter {field} to search: ").strip()
            results = lib.search_books(query, field)
            if results:
                print("Search results:")
                for book in results:
                    print(book)
            else:
                print("No books found.")
                
        elif choice == "3": # Option 3: Update information about an existing book
            id_input = input("Enter book ID to update: ").strip()
            try:
                book_id = int(id_input)
            except ValueError:
                print("Invalid book ID.")
                continue
            print("Leave field empty if you don't want to update it.")
            title = input("Enter new title: ").strip()
            author = input("Enter new author: ").strip()
            genre = input("Enter new genre: ").strip()
            year_input = input("Enter new publication year(only the year): ").strip()
            year = None
            if year_input:
                try:
                    year = int(year_input)
                except ValueError:
                    print("Invalid year input (list only the year).")
                    continue
            updated_book = lib.update_book(book_id, title or None, author or None, genre or None, year)
            if updated_book:
                print("Book updated:")
                print(updated_book)
                
        elif choice == "4": # Option 4: Remove a book from the collection
            id_input = input("Enter book ID to remove: ").strip()
            try:
                book_id = int(id_input)
            except ValueError:
                print("Invalid book ID.")
                continue
            removed = lib.remove_book(book_id)
            if removed:
                print("Book removed:")
                print(removed)
                
        elif choice == "5": # Option 5: Display all books in the library
            books = lib.display_books()
            if books:
                print("Books in the library:")
                for book in books:
                    print(book)
            else:
                print("No books in the library.")
                
        elif choice == "6": # Option 6: Display books based on specific criteria
            print("Display by criteria:")
            print("a. Recently added")
            print("b. By genre")
            crit_choice = input("Enter choice (a/b): ").strip().lower()
            if crit_choice == "a":
                books = lib.display_books(criteria="recent")
                print("Recently added books:")
                for book in books:
                    print(book)
            elif crit_choice == "b":
                genre_dict = lib.display_books(criteria="genre")
                for genre, books in genre_dict.items():
                    print(f"\nGenre: {genre}")
                    for book in books:
                        print(book)
            else:
                print("Invalid criteria choice.")
                
        elif choice == "7": # Option 7: Show a set of unique authors from the library
            authors = lib.get_unique_authors()
            print("Unique authors:")
            for author in authors:
                print(author)
                
        elif choice == "8": # Option 8: Show a set of unique genres from the library
            genres = lib.get_unique_genres()
            print("Unique genres:")
            for genre in genres:
                print(genre)
                
        elif choice == "9": # Option 9: Exit the program
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
