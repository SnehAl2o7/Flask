from flask import Flask, render_template , url_for

app = Flask(__name__)

posts = [
    {
        'author': 'TEst-data',
        'title': 'Blog Post',
        'content': 'First POst',
        'data_posted': 'July 30, 2026'
    },
    {
        'author': 'TEst-data-1',
        'title': 'Blog Post-2',
        'content': 'Second POst',
        'data_posted': 'July 31, 2026'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)