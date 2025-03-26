import csv
from datetime import datetime

class Book:
    """
    Represents a book in the library.
    
    Attributes:
        book_id (int): Unique identifier.
        title (str): Title of the book.
        author (str): Author of the book.
        genre (str): Genre of the book.
        year (int): Publication year.
        added_date (str): Date the book was added.
    """
    
    def __init__(self, book_id, title, author, genre, year, added_date=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        if added_date is None:
            self.added_date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.added_date = added_date
    
    def to_dict(self):
        """
        Returns a dictionary rep of the book.
        """
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "year": self.year,
            "added_date": self.added_date
        }
    
    def update(self, title=None, author=None, genre=None, year=None):
        """
        Updates the books attributes.
        """
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if year:
            self.year = year
    
    def __str__(self):
        return (f"[{self.book_id}] {self.title} by {self.author} "
                f"({self.year}) - Genre: {self.genre} (Added: {self.added_date})")

class FictionBook(Book):
    """
    Represents a Fiction book.
    """
    def __init__(self, book_id, title, author, genre, year, added_date=None):
        super().__init__(book_id, title, author, genre, year, added_date)
        self.fiction = True

class NonFictionBook(Book):
    """
    Represents a Non-Fiction book.
    """
    def __init__(self, book_id, title, author, genre, year, added_date=None):
        super().__init__(book_id, title, author, genre, year, added_date)
        self.fiction = False

class Library:
    """
    Manages a collection of books.
    
    Attributes:
        books (dict): A dictionary mapping book_id to Book objects.
        next_id (int): The next available book ID.
        csv_file (str): The CSV file path.
    """
    
    def __init__(self, csv_file="books.csv"):
        self.books = {}
        self.csv_file = csv_file
        self.next_id = 1
        self.load_books()
    
    def load_books(self):
        """
        Loads books from the CSV file.
        """
        try:
            with open(self.csv_file, mode="r", newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book_id = int(row["book_id"])
                    title = row["title"]
                    author = row["author"]
                    genre = row["genre"]
                    year = int(row["year"])
                    added_date = row.get("added_date", "")
                    
                    # Determine class based on genre
                    if genre.lower() in ["fiction", "novel", "fantasy", "mystery"]:
                        book = FictionBook(book_id, title, author, genre, year, added_date)
                    else:
                        book = NonFictionBook(book_id, title, author, genre, year, added_date)
                    self.books[book_id] = book
                    if book_id >= self.next_id:
                        self.next_id = book_id + 1
        except FileNotFoundError:
            print(f"CSV file '{self.csv_file}' not found. Starting with an empty library.")
    
    def save_books(self):
        """
        Saves the book collection to the CSV file.
        """
        try:
            with open(self.csv_file, mode="w", newline='', encoding="utf-8") as file:
                fieldnames = ["book_id", "title", "author", "genre", "year", "added_date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.books.values():
                    writer.writerow(book.to_dict())
        except Exception as e:
            print("Error saving books:", e)
    
    def add_book(self, title, author, genre, year):
        """
        Adds a new book and saves the updated collection.
        """
        if genre.lower() in ["fiction", "novel", "fantasy", "mystery"]:
            book = FictionBook(self.next_id, title, author, genre, year)
        else:
            book = NonFictionBook(self.next_id, title, author, genre, year)
        self.books[self.next_id] = book
        self.next_id += 1
        self.save_books()
        return book
    
    def search_books(self, query, field="title"):
        """
        Searches for books by field.
        
        Returns a list of books matching query.
        """
        query = query.lower()
        results = [book for book in self.books.values() if query in getattr(book, field).lower()]
        return results
    
    def update_book(self, book_id, title=None, author=None, genre=None, year=None):
        """
        Updates the book by book_id.
        """
        if book_id in self.books:
            self.books[book_id].update(title, author, genre, year)
            self.save_books()
            return self.books[book_id]
        else:
            print("Book ID not found.")
            return None
    
    def remove_book(self, book_id):
        """
        Removes a book from the collection.
        """
        if book_id in self.books:
            removed = self.books.pop(book_id)
            self.save_books()
            return removed
        else:
            print("Book ID not found.")
            return None
    
    def display_books(self, criteria=None):
        """
        Returns books based on criteria.
        
        If criteria is recent, it returns books sorted by added_date in descending order.
        If criteria is genre, it returns a dictionary grouping books by genre.
        Otherwise, returns all books.
        """
        if criteria == "recent":
            return sorted(self.books.values(), key=lambda b: b.added_date, reverse=True)
        elif criteria == "genre":
            genre_dict = {}
            for book in self.books.values():
                genre_dict.setdefault(book.genre, []).append(book)
            return genre_dict
        else:
            return list(self.books.values())
    
    def get_unique_authors(self):
        """
        Returns unique authors.
        """
        return {book.author for book in self.books.values()}
    
    def get_unique_genres(self):
        """
        Returns unique genres.
        """
        return {book.genre for book in self.books.values()}
