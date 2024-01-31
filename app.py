from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def grid():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/products')
def product():
    return render_template("product.html")

if __name__ == '__main__':
    app.run(debug=True)