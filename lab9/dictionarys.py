books = []

book = {
    "author": "Charles Dickens",
    "title": "Great Expectations",
}

print(f"Author: {book['author']}")
books.append(book)

book = {
    "author": "Dr. Seuss",
    "title": "Green Eggs and Ham",
}
books.append(book)

print(f"Books List: {books}")

for book in books:
    print(book)
print(f"First Books Author: {books[0]['author']}")