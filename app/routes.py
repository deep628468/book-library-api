from flask import Blueprint, jsonify, request
from app.models.book import Book
from app import db

books_bp = Blueprint("books", __name__)


@books_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()

    return jsonify([book.to_dict() for book in books])


@books_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book.to_dict())


@books_bp.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    if "title" not in data or "author" not in data:
        return jsonify({"error": "Title and author are required"}), 400 
    
    if not isinstance(data["title"], str) or not data["title"].strip():
        return jsonify({"error": "Title must be a non-empty string"}), 400

    if not isinstance(data["author"], str) or not data["author"].strip():
        return jsonify({"error": "Author must be a non-empty string"}), 400
    
    book = Book(
        title=data["title"],
        author=data["author"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 201


@books_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
      
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    if "title" not in data or "author" not in data:
        return jsonify({"error": "Title and author are required"}), 400
    
    if not isinstance(data["title"], str) or not data["title"].strip():
        return jsonify({"error": "Title must be a non-empty string"}), 400

    if not isinstance(data["author"], str) or not data["author"].strip():
        return jsonify({"error": "Author must be a non-empty string"}), 400


    book.title = data["title"]
    book.author = data["author"]

    db.session.commit()

    return jsonify(book.to_dict())

@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully"})