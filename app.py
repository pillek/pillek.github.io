from flask import Flask, flash, redirect, render_template, request,jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from db import Advisor
from forms import RegistrationForm, LoginForm
import os 
from mailjet_rest import Client

api_key = '0ea29243b0002891e017d12b70a4bbda'
api_secret = 'e83685e4f462e8cf40097d9b895ac6a1'
mailjet = Client(auth=(api_key, api_secret))

app = Flask(__name__)
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dont-know'
db = SQLAlchemy(app)

from models import Login, Customer, Consultant, CustomerRequest, ConsultantResponse

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/singleadvisor')
def singleadvisor():
    return render_template('singleadvisor.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        advisor = Advisor.query.filter_by(usermail = form.usermail.data).first()
        if advisor and advisor.password == form.password.data:
            flash('Login successful!')
    return render_template('login.html', form = form)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()  # Initialisiere form als Instanz von RegistrationForm
    if request.method == 'POST':
        advisor = Advisor(usermail=request.form.get('usermail'),
                          password=request.form.get('password'),
                          name=request.form.get('name'),
                          description=request.form.get('description'))
        db.session.add(advisor)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

     return render_template('dashboard.html')

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
    db.create_all()  # Erstelle die Tabellen in der Datenbank
    app.run(debug=True)