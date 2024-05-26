from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "year": 1},
    {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2},
    {"id": 3, "title": "Book 3", "author": "Author 3", "year": 3}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return render_template('book.html', book=book)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_id = max(book['id'] for book in books) + 1
        new_book = {
            "id": new_id,
            "title": request.form['title'],
            "author": request.form['author'],
            "year": int(request.form['year'])
        }
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)

