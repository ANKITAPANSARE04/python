from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    # return render_template('contact.html')
    return render_template('contact.html',  my_data=[6,7,8,9,10,11])


app.run(debug=True)

