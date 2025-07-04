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

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/greet')
def greet():
    user = request.args.get('user', 'Friends')
    return render_template('greet.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # You can add validation here if needed
        return redirect(url_for('secure'))
    return render_template('login.html')

@app.route('/secure')
def secure():
    return render_template('secure.html')

if __name__ == '__main__':
    app.run(debug=True)
