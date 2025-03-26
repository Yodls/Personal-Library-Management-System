Personal Library Management System
___________________________________________________________________________________________________________________________
Instructions for Running and Using:

To run, open a terminal and naviagte to the folder containing the program and run:
   python3 main.py

To use this program, select an option between 1-9. Below are the descriptions and instructions for each option;

1: Adds new books. You must enter the title, author, genre(can be any genre), and publication year

2: Searches for books. You must choose if you want to search by title, author, or genre,
then type in the title, author, or genre to search.

3: Updates a book. You must first identify the book id by listing all books( option 5), and then select
id for update. You can then choose to edit the fields one by one, or leave them as is if you dont want to update anything.

4: Removes a book by book id.

5: Displays all stored books.

6: Display books by criteira, option a shows books that have been recently added (lists books from most recently added),
and option b lists the books by genre.

7: Displays the unique authors that are stored.

8: Displays the unique genres stored. 

9: Exits the program.
___________________________________________________________________________________________________________________________
Features Implemented:
- Add new books to the collection.
- Search for books by title, author, or genre.
- Update existing book information.
- Remove books from the collection.
- Display all books, or filter by criteria (recently added, by genre).
- Display unique authors and genres.
- Data is persistent using CSV file I/O.
- OOP design with classes, inheritance, and methods.
- Using dictionaries, list comprehensions, and sets.
- Input validation with error checking.
___________________________________________________________________________________________________________________________
Known Issues:
- Input validation could be more robust for errors.
- Genre tyoes for fiction vs. non-fiction is very basic and provides little information.
___________________________________________________________________________________________________________________________
References:
- Think Python 3e by Allen Downey (Chapters 10, 14, 15, 16)
