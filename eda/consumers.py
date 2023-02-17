from flask import Flask, request, session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'45861e0eb8863ac8d372ecf42adf32bd64f83ff7b5201e9a161e59bd58ddd444'

# @app.route('/')
# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))


@app.route('/notification', methods=["POST"])
def notification_consumer():
    return "Success"

@app.route('/post', methods=["POST"])
def post_consumer():
    print('posted')
    post = request.get_json(force=True) 
    return post