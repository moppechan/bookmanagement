from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    msg = request.args.get('msg')   # Redirect された時のパラメータ受け取り

    if msg == None:
        # 通常のアクセスの場合
        return render_template('index.html')
    else :
        # register_exe() から redirect された場合
        return render_template('index.html', msg=msg)

@app.route('/', methods=['POST'])
def login():
    user_name = request.form.get('username')
    password = request.form.get('password')
    
    # ログイン判定
    if db.login(user_name, password):
        return redirect(url_for('top'))
    else:
        error = 'ユーザ名またはパスワードが違います。'
        
        # dictで返すことでフォームの入力量が増えても可読性が下がらない。
        input_data={'user_name':user_name, 'password':password}
        return render_template('index.html', error=error, data=input_data)
    
@app.route('/top', methods=['GET'])
def top():
    return render_template('top.html')   
   
@app.route('/register')
def register_form():
    return render_template('register.html')

@app.route('/register_exe', methods=['POST'])
def register_exe():
    user_name = request.form.get('username')
    password = request.form.get('password')

    # バリデーションチェック
    if user_name == '':
        error = 'ユーザ名が未入力です'
        return render_template('register.html', error=error)

    if password == '':
        error = 'パスワードが未入力です'
        return render_template('register.html', error=error)

    count = db.insert_user(user_name, password)

    if count == 1:
        msg = '登録が完了しました。'
        return redirect(url_for('index', msg=msg))  # Redirect で index()に Get アクセス
        # return render_template('index.html', msg=msg)
    else:
        error = '登録に失敗しました。'
        return render_template('register.html', error=error)    

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