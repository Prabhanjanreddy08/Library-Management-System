from flask import Blueprint, request
from models import Book
from utils import validate_request_json, paginate_items, create_response
from auth import token_required

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=["GET"])
@token_required
def get_books():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    search = request.args.get("search", "")

    books = [book for book in Book.books if search.lower() in (book["title"] + book["author"]).lower()]
    paginated_result = paginate_items(books, page, per_page)
    return create_response(paginated_result)

@books_bp.route("/books", methods=["POST"])
@token_required
def add_book():
    is_valid, error = validate_request_json(["title", "author"])
    if not is_valid:
        return create_response({"error": error}, 400)

    data = request.get_json()
    book = Book.add_book(data["title"], data["author"])
    return create_response(book, 201)

@books_bp.route("/books/<int:book_id>", methods=["PUT"])
@token_required
def update_book(book_id):
    is_valid, error = validate_request_json(["title", "author"])
    if not is_valid:
        return create_response({"error": error}, 400)

    data = request.get_json()
    book = Book.update_book(book_id, data["title"], data["author"])
    if book:
        return create_response(book)
    return create_response({"error": "Book not found"}, 404)

@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
@token_required
def delete_book(book_id):
    book = Book.delete_book(book_id)
    if book:
        return create_response({"message": "Book deleted"})
    return create_response({"error": "Book not found"}, 404)
