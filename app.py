from flask import Flask, render_template, redirect, url_for, session, request,flash
from flask_mysqldb import MySQL
import MySQLdb
import mysql.connector

app = Flask(__name__)
app.secret_key = "1234353234"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Revanth_22"
app.config["MYSQL_DB"] = "hackathon"

db = MySQL(app)







@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'Email' in request.form and 'password' in request.form:
            Email = request.form['Email']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM logininfo WHERE Email=%s AND Password= %s", (Email,password))
            info = cursor.fetchone()
            if info is not None:
                if info['Email'] == Email and info['Password'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for('home'))

            else:
                return redirect(url_for('login'))
                #return redirect(url_for('index'))


    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO hackathon.logininfo(Name, Password, Email)VALUES(%s,%s,%s)",(username,password,email))
            db.connection.commit()
            return redirect(url_for('login'))
        else:
            return render_template("signup.html")



    return render_template("signup.html")





@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")


@app.route('/bot')
def bot():
    return render_template("bot.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        if "firstname" in request.form and "lastname" in request.form and "PersonalMail" in request.form and "City" in request.form and "State" in request.form and "Issues" in request.form :
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            PersonalMail = request.form['PersonalMail']
            City = request.form['City']
            State = request.form['State']
            Issues = request.form['Issues']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO hackathon.reports(First_Name, Last_Name, Phone_Number, City, State, Issue)VALUES(%s,%s,%s,%s,%s,%s)",(firstname,lastname,PersonalMail,City,State,Issues))
            db.connection.commit()
            return redirect(url_for('home'))
        else:
            return render_template("contact.html")

    return render_template("contact.html")




@app.route('/logout')
def logout():
    session.pop('loginsuccess',None)
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
