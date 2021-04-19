from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "christiano wuz here"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/valid', methods=["post"])
def valid():
    is_valid = True
    if (len(request.form['email']) < 1):
        is_valid = False
        flash("Email can not be blank!")
        return redirect('/')
    else:
        flash("SUCCESS NEW EMAIL ACQUIRED YO")
        query = 'INSERT INTO email (email, created_at, updated_at) VALUES (%(email)s, NOW(),NOW());'
        data = {"email": request.form['email']}
        connectToMySQL('email_db').query_db(query,data)
        return redirect('/success')

@app.route('/success')
def success():
    query = 'SELECT * FROM email;'
    results = connectToMySQL('email_db').query_db(query)
    return render_template('success.html', results = results)


if __name__ == "__main__":
    app.run(debug=True)