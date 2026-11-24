from book import Book
from library import Library

library = Library()

def remove_book():
    pass

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    genre = input("Enter the book genre: ")

    new_book = Book(title, author, genre)
    
    library.add_book(new_book)

def list_books():
    for book in library:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Status: {book.get_state()}")

def display_menu():
    print("1. Add Book")
    print("2. Remove Book")
    print("3. List All Books")
    print("4. Find Book")
    print("5. Check Out Book")
    print("6. Return Book")
    print("7. Exit")

def main():
    while True:
        display_menu()
        selection = int(input("Enter your selection: "))

        match selection:
            case 1:
                add_book()
            case 2:
                remove_book()
            case 3:
                list_books()
            case 6:
                exit()

 
main()