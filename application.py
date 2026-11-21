from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author}"
    

    

@app.route('/books')
def get_books():
    books = Book.query.all()
    return {"books": [{"id": book.id, "book_name": book.book_name, "author": book.author, 
                       "publisher": book.publisher} for book in books]}

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
