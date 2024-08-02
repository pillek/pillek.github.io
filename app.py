from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from mailjet_rest import Client

api_key = '0ea29243b0002891e017d12b70a4bbda'
api_secret = 'e83685e4f462e8cf40097d9b895ac6a1'
mailjet = Client(auth=(api_key, api_secret))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advisor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mail = Mail(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from database import db
db.init_app(app)
from models import User # use model for the user
from forms import RegistrationForm, LoginForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/singleadvisor')
def singleadvisor():
    return render_template('singleadvisor.html')

@app.route('/about')
def aboutus():
    return render_template('aboutus.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route("/dashboard")
@login_required
def dashboard():
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     preferences = request.form.get('preferences')
    #     biography = request.form.get('biography')
    #     return 'Erfolgreich abgesendet!'
    return render_template('dashboard.html', title='Dashboard')

@app.route('/home',methods=['GET', 'POST'])
# new
@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/advisors')
def advisors():
    return render_template('advisors.html')


@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    email = data['email']
    subject = data['subject']
    message_body = data['message']

    data = {
        'FromEmail': 'tippitopp034@gmail.com',
        'FromName': 'Fashion Website',
        'Subject': subject + ' - ' + email,
        'Text-part': message_body,
        'Html-part': message_body,
        'Recipients': [{'Email': 'tippitopp034@gmail.com'}]
    }

    try:
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
        return jsonify({"status": "success", "message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    print("Received payment data:")
    print("Order details:")
    print(f"Service: {data['order']['service']}")
    print(f"Price: €{data['order']['price']}")
    print("\nPayment details:")
    print(f"Card Number: {data['payment']['cardNumber']}")
    print(f"Cardholder Name: {data['payment']['cardholderName']}")
    print(f"Expiry Date: {data['payment']['expiryDate']}")
    print(f"CVV: {data['payment']['cvv']}")

    # Here you would typically process the payment with a payment gateway

    return jsonify({"message": "Payment processed successfully"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)