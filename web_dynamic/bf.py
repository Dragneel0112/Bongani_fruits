#!/usr/bin/python3
'''
Application for Bongani fruits
'''
from flask import Flask, render_template, url_for,  redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'bonganifruitskey'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a new one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
@app.route('/home')
def home():
    '''
    Homepage before login
    '''
    return render_template('home.html')


@app.route('/products')
def products():
    '''
    Products page
    '''
    return render_template('products.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Login route for application
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home_p'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Register new User
    '''
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    '''
    Logout User
    '''
    logout_user()
    return redirect(url_for('home'))


@app.route('/home_p', methods=['GET', 'POST'])
@login_required
def home_p():
    '''
    Login Homepage
    '''
    return render_template('home_p.html')


@app.route('/products_cart', methods=['GET', 'POST'])
@login_required
def products_cart():
    '''
    Products page with cart
    '''
    return render_template('products_cart.html')


if __name__ == "__main__":
    '''
    App fucnction with debug
    '''
    app.run(host='0.0.0.0', port=5000, debug=True)
