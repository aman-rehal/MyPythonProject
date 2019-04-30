import json

from auth import oidc
from flask import request

from encode.encoder import DateTimeEncoder
from model.models import Author

from flask import Blueprint

author_bp = Blueprint('author_bp', 'author_bp', url_prefix='/api')


@author_bp.route("/author", methods=['POST'])
@oidc.accept_token(True)
def add_author():
    author = Author(name=request.form['name'], email=request.form['email'])
    author.save()
    return json.dumps(author, cls=DateTimeEncoder)


@author_bp.route("/author")
@oidc.accept_token(True)
def get_author():
    all_authors = Author.query.all()
    return json.dumps(all_authors, cls=DateTimeEncoder)
