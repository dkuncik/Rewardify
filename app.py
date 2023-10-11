from flask import Flask

app = Flask(__name__)


# TODO: Installation Route
@app.route('/install')
def install():
    ...


# TODO: Home Route
@app.route('/')
def home():
    ...


# TODO: Login Route
@app.route('/login')
def login():
    ...


# TODO: Logout Route
@app.route('/logout')
def logout():
    ...


# TODO: Dashboard Route
@app.route('/dashboard')
def dashboard():
    ...


# TODO: Customers Route
@app.route('/customers')
def customers():
    ...


# TODO: Employees Route
@app.route('/employees')
def employees():
    ...


# TODO: Products Route
@app.route('/products')
def products():
    ...


# TODO: Settings Route
@app.route('/settings')
def settings():
    ...


# TODO: Statistics Route
@app.route('/statistics')
def statistics():
    ...


if __name__ == '__main__':
    app.run()
