import json

from auth import oidc
from flask import request

from encode.encoder import DateTimeEncoder
from model.models import Author, Book

from flask import Blueprint

book_bp = Blueprint('book_bp', 'book_bp', url_prefix='/api')


@book_bp.route("/book", methods=['POST'])
@oidc.accept_token(True)
def add_book():
    author_email_id = request.form['author_email_id']
    author = Author.query.filter(Author.email == author_email_id).first()

    book = Book(title=request.form['title'], author=author, year=int(request.form['year']))
    book.save()
    return json.dumps(book, cls=DateTimeEncoder)


@book_bp.route("/book")
@oidc.accept_token(True)
def get_book():
    all_books = Book.query.all()
    return json.dumps(all_books, cls=DateTimeEncoder)
