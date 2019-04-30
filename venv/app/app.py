from flask import Flask

from author.authorController import author_bp
from book.bookController import book_bp
from db_config import db
from auth import oidc

app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'library'
db.init_app(app)

app.register_blueprint(author_bp)
app.register_blueprint(book_bp)

app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'OIDC_CLIENT_SECRETS': './client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_SCOPES': ["openid", "profile", "email"],
    'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
})


oidc.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
