from flask import render_template,request,redirect,url_for,session, flash
from . import app, mysql, bcrypt



@app.route("/")
def base():
    return render_template('base.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT email, password FROM tbl_user WHERE email = '{email}'")
        user = cur.fetchone()
        cur.close()

        if user and password == user[1]:
            print("Login successful. Redirecting to 'base'.")
            session['email'] = user[0]
            return redirect(url_for('base'))
        else:
            print("Login failed. Invalid email or password.")
            flash('Invalid email or password', 'error')
            return render_template("login.html", error='Invalid email or password')

    return render_template('login.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_user (name, email, phone, password) VALUES (%s, %s, %s, %s)",(name, email, phone, password))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route("/about")
def about():
    return render_template('about_us.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/service_danaTunai", methods = ['GET', 'POST'])
def service_danaTunai():
    if request.method == 'POST':
        jumlah_peminjaman = request.form['jumlah_peminjaman']
        periode_peminjaman = request.form['periode_peminjaman']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO dana_tunai (jumlah_peminjaman, periode_peminjaman) VALUES (%s, %s)", (jumlah_peminjaman,periode_peminjaman))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('service_danaTunai'))
    return render_template('service_danaTunai.html')

@app.route("/home")
def home():
    return render_template('base.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')



if __name__ == "__main__":
    app.run(debug=True)