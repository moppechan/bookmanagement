from flask import Flask, render_template, request, redirect, url_for, session
import db, string, random
from book import book_bp

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_letters, k=256))

# BluePrint登録
app.register_blueprint(book_bp)


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
        session['user'] = True
        return redirect(url_for('top'))
    else:
        error = 'ユーザ名またはパスワードが違います。'
        
        # dictで返すことでフォームの入力量が増えても可読性が下がらない。
        input_data={'user_name':user_name, 'password':password}
        return render_template('index.html', error=error, data=input_data)
    
@app.route('/top', methods=['GET'])
def top():
    if 'user' in session:
        return render_template('top.html')   
    else :
        return redirect(url_for('index'))
   
@app.route('/logout')
def logout():
    session.pop('user', None)   # sessionの破棄
    return redirect(url_for('index'))   # ログイン画面にリダイレクト
   
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

if __name__ == '__main__':
    app.run(debug=True)