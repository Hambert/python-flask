from flask import Flask, abort, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'9\xb4\xa1D\xe8%R\xd4'

@app.route('/')
def index():
    if 'username' in session:
        return '''<p>You are logged in as %s</p>
                  <a href="/logout">Logout</a>
                ''' % escape(session['username'])
    return '''<p>You are not logged in</p>
                <a href="/login">Login</a> 
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/me")
def me_api():
    if 'username' in session:
        return {
            "username": escape(session['username']),
        }
    else:
        abort(401)

@app.errorhandler(404)
def page_not_found(error):
    abort(404)

if __name__ == '__main__': 
    # running app 
    app.run(use_reloader = True, debug = False) 