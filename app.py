from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm
import os 

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
    return render_template('login.html', form = form)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        form = RegistrationForm
        usermail = request.form.get('usermail')
        password = request.form.get('password')

    return render_template('registration.html', form = form)

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     preferences = request.form.get('preferences')
    #     biography = request.form.get('biography')
    #     return 'Erfolgreich abgesendet!'
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

    msg = Message(
        subject,
        sender='tippitopp034@gmail.com',
        recipients=[email]
    )
    msg.body = message_body

    try:
        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



if __name__ == '_main_':
    db.create_all()  # Erstelle die Tabellen in der Datenbank
    app.run(debug=True)
