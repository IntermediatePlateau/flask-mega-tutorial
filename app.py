from flask import render_template, flash, redirect
from flask import Flask
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'}, # I used a comma here instead of : and it caused an error 
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # I forgot the brackets here and it broke
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


# Continue from part 3 Improving Field Validation
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

