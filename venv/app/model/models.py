from db_config import db


class Author(db.Document):
    name = db.StringField()
    email = db.StringField()

    def __str__(self):
        return self.name + self.email


class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField()

    def __str__(self):
        return self.title + self.author + self.year
