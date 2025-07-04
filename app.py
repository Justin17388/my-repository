# # Import Flask modules
# from flask import Flask, render_template, request

# # Create an object named app
# app = Flask(__name__)

# # Create welcome page with main.html file and assign it to the root path
# @app.route('/')
# def home():
#     return render_template('main.html')

# # Write a function named `greet`
# @app.route('/greet')
# def greet():
#     user = request.args.get('user', 'Friends')  # Default to 'Friends'
#     return render_template('greet.html', user=user)


# # Write a function named `login`
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         return render_template('secure.html', username=username)
#     return render_template('login.html')

# # Add a statement to run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)

# Reformatted  for better flow
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html') # Main now has a greet page link.

@app.route('/greet')
def greet():
    user = request.args.get('user', 'Friends')
    return render_template('greet.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # For now we're not using the password. It can be saved to a SQlite later though.
        return redirect(url_for('secure', username=username))
    return render_template('login.html')

@app.route('/secure')
def secure():
    username = request.args.get('username', 'Guest')
    return render_template('secure.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

