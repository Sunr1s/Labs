class Book:
    def __init__(self, code, author, title, year_of_publication):
        self.code = code
        self.author = author
        self.title = title
        self.year_of_publication = year_of_publication

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year_of_publication})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def count_books_published_after(self, year):
        return len([book for book in self.books if book.year_of_publication > year])


if __name__ == "__main__":
    library = Library()

    library.add_book(Book(1, "Author A", "Book 1", 2000))
    library.add_book(Book(2, "Author B", "Book 2", 2001))
    library.add_book(Book(3, "Author A", "Book 3", 2002))
    library.add_book(Book(4, "Author C", "Book 4", 2003))
    library.add_book(Book(5, "Author B", "Book 5", 2004))

    author_to_search = "Author A"
    books_by_author = library.get_books_by_author(author_to_search)
    print(f"Books by {author_to_search}:")
    for book in books_by_author:
        print(book)

    year_to_search = 2001
    num_books_published_after = library.count_books_published_after(year_to_search)
    print(f"Number of books published after {year_to_search}: {num_books_published_after}")

