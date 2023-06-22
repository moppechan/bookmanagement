from flask import Flask, render_template, request, redirect, url_for
import bookdb as db

app = Flask(__name__)

@app.route('/bookregi')
def bookregi():
    return render_template('bookregi.html')

@app.route('/bookregi_exe', methods=["POST"])
def bookregi_exe():
    title = request.form.get('title')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    isbn = request.form.get('isbn')
    
    db.insert_book(title, author, publisher, isbn)
    
    book_list = db.select_all_books()
    
    return render_template('list.html', books=book_list)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/list')
def list():
    book_list = db.select_all_books()
    return render_template('list.html', books=book_list)

if __name__ == "__main__":
    app.run(debug=True)