# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# Create welcome page with main.html file and assign it to the root path
@app.route('/')
def home():
    return render_template('main.html')

# Write a function named `greet`
@app.route('/greet')
def greet():
    user = request.args.get('user')
    if user:
        return render_template('greet.html', user=user)
    else:
        return "⚠️ Please provide a user parameter in the URL like /greet?user=YourName"

# Write a function named `login`
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return render_template('secure.html', username=username)
    return render_template('login.html')

# Add a statement to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

