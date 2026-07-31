from flask import Flask, render_template , url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e797e470a55acd755fef9f2e6029d494'

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

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)