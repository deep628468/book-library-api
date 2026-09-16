from app.models.book import Book
from app import db

def get_all_books():
    return Book.query.all()

def get_book_by_id(book_id):
    return Book.query.get(book_id)

def create_book(title, author):
    book = Book(
        title=title,
        author=author
    )

    db.session.add(book)
    db.session.commit()

    return book

def update_book(book_id, title, author):
    book = Book.query.get(book_id)

    if book is None:
        return None

    book.title = title
    book.author = author

    db.session.commit()

    return book 

def delete_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return False

    db.session.delete(book)
    db.session.commit()

    return True