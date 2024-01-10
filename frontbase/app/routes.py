from flask import render_template
from app import app



@app.route("/")
def base():
    return render_template('base.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/about")
def about():
    return render_template('about_us.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/service_danaTunai")
def service_danaTunai():
    return render_template('service_danaTunai.html')

@app.route("/home")
def home():
    return render_template('base.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')



if __name__ == "__main__":
    app.run(debug=True)

# from app import app