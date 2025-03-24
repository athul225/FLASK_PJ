from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)
con=sqlite3.connect('user.db')
con.execute('''
           CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
            )
            ''')
con.commit()


@app.route("/index",methods=["GET","POST"])
def index():
    message=""
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        try:
            con=sqlite3.connect('user.db')
            con.execute("INSERT INTO users (name,email) VALUES(?,?)",(name,email))
            con.commit()
            message="Data save aayittund ketto....."
        except:
            message='Data save cheyyan sweekarikkilla....'
    return render_template('index.html',message=message)

if __name__ == '__main__':
    app.run(debug=True)