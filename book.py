from flask import Blueprint, render_template, request, redirect, url_for
import bookdb as db

book_bp = Blueprint('book', __name__, url_prefix='/book')

# app = Flask(__name__)

@book_bp.route('/bookregi')
def bookregi():
    return render_template('bookregi.html')

@book_bp.route('/bookregi_exe', methods=["POST"])
def bookregi_exe():
    title = request.form.get('title')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    isbn = request.form.get('isbn')
    
    db.insert_book(title, author, publisher, isbn)
    return render_template('regiresult.html', title=title, author=author, publisher=publisher, isbn=isbn)

@book_bp.route('/delete')
def delete():
    return render_template('delete.html')

@book_bp.route('/delete_exe', methods=["POST"])
def delete_exe():
    id = request.form.get('id')
    
    db.delete_book(id)
    return render_template('delresult.html', id=id)

@book_bp.route('/list')
def list():
    book_list = db.select_all_books()
    return render_template('list.html', books=book_list)

@book_bp.route('/userlist')
def userlist():
    book_list = db.select_all_books()
    return render_template('userlist.html', books=book_list)
