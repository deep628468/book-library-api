from flask import Blueprint, jsonify, request
from app.services.book_service import (
    get_all_books,
    get_book_by_id,
    create_book as create_book_service,
    update_book as update_book_service,
    delete_book as delete_book_service
)

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=["GET"])
def get_books():
    books = get_all_books()
    return jsonify([book.to_dict() for book in books])


@books_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = get_book_by_id(book_id)

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

    book = create_book_service(
        title=data["title"].strip(),
        author=data["author"].strip()

    )

    return jsonify(book.to_dict()), 201


@books_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    if "title" not in data or "author" not in data:
        return jsonify({"error": "Title and author are required"}), 400

    if not isinstance(data["title"], str) or not data["title"].strip():
        return jsonify({"error": "Title must be a non-empty string"}), 400

    if not isinstance(data["author"], str) or not data["author"].strip():
        return jsonify({"error": "Author must be a non-empty string"}), 400

    book = update_book_service(
        book_id=book_id,
        title=data["title"].strip(),
        author=data["author"].strip()
    )

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book.to_dict())


@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    deleted = delete_book_service(book_id)

    if not deleted:
        return jsonify({"error": "Book not found"}), 404

    return jsonify({"message": "Book deleted successfully"})

