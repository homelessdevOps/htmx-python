from app import db

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", backref="author")

    # Was  passiert wenn ich die Klasse toString mache, so sieht
    # es dann besser aus.
    # https://www.pythontutorial.net/python-oop/python-__repr__/
    def __repr__(self):
        return '<Author: {}>'.format(self.books)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.author_id"))
    title = db.Column(db.String)
