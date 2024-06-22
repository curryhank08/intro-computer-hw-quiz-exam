"""
author: H24111057 姚博瀚
"""

library = {}

def menu():
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    book_info = input("Enter book title, genre, and price separated by '|': ").split("|")
    title = book_info[0].strip()
    genre = book_info[1].strip()
    price = float(book_info[2].strip())

    library[title] = [genre, price]
    print()
    print(f"Added '{title}' to the library.")
    print()
    return True

def remove_book(): 
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    title = input("Enter the title of the book you want to remove: ").strip()
    print()
    if title in library:
       del library[title]
       print(f"'{title}' has been removed from the library.")
       return True
    else:
       print(f"Error: '{title}' is not in the library.")
    

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """
    title = input("Enter the title of the book you want information about: ").strip()
    if title in library:
        genre, price = library[title]
        print(f"Title: {title}\nGenre: {genre}\nPrice: ${price:.2f}")
    else:
        print(f"Error: '{title}' is not in the library.")

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("There are no books in the library.")
    else:
        print("All books in the library:")
        for title in sorted(library):
            genre, price = library[title]
            print(f"Title: {title} (Genre: {genre}, Price: ${price:.2f})")

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    genre = input("Enter the genre you want to list books for: ").strip()
    found_books = False
    for title, book_info in library.items():
        if book_info[0] == genre:
            print(f"Title: {title} (Genre: {book_info[0]}, Price: ${book_info[1]:.2f})")
            found_books = True
    if not found_books:
        print(f"No books found in the '{genre}' genre.")

def main():
    
    while True:
        print()
        menu()
        choice = input("Enter your choice (1-6): ").strip()
        print()
        if choice == "1":
            add_book_return = add_book()
            if add_book_return:
                list_books()
                print()
        elif choice == "2":
            remove_book_return = remove_book()
            if remove_book_return:
                list_books()
                print()
        elif choice == "3":
            get_book_info()
            print()
        elif choice == "4":
            list_books()
            print()
        elif choice == "5":
            list_books_by_genre()
            print()
        elif choice == "6":
            print("Goodbye!")
            print()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
   main()