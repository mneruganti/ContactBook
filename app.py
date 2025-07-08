# Import modules
from flask import Flask, render_template, request, redirect, url_for
from models import db, Contact

app = Flask(__name__)

# defined where the database is -> uses a SQLite file called contacts.db in this folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'

# this tracks objects changes and sends signals, so we disable it to reduce wait times
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# we can initialize the database here and connect the DB with the app
db.init_app(app)

# app_context() gives info about the app to create_all()
with app.app_context(): 
    
    # This tells SQLAlchemy to create tables based on 'Contact' class (the model)
    db.create_all()

# Defines a route to the homepage
@app.route('/')
def index():
    
    # Fetches all saved contacts from the database and stores it
    contacts = Contact.query.all()
    
    # Send these contacts to html file
    return render_template('index.html', contacts=contacts)

# Defines another route to add a contact. This accepts GET, which displays the form,
# and POST, which processes the form information
app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method() == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']  
    

