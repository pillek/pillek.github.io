from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form.get('name')
        preferences = request.form.get('preferences')
        biography = request.form.get('biography')
        return 'Erfolgreich abgesendet!'
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)