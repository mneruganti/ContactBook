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
    # If the method is asked to process information given in the form
    if request.method() == 'POST':
        
        # Use request.form to get information from the HTML form
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        
        # Create a new Contact
        contact = Contact(name=name, phone=phone, email=email)
        
        # Add it to the session
        db.session.add(contact)
        
        # Commit the changes to the database
        db.session.commit()
        
        # Send back to homepage
        return redirect('/')
    
    # Otherwise, send the current information to the HTML file and update it
    return render_template('add_contact.html')

# This defines a dynamic URL that changes based on the ID of the contact. This method
# takes in the specific ID
@app.route('/edit/<int:id>', methods=['GET', 'POST'])  
def edit_contact(id):
    
    # This line gets the contact of the ID or returns a 404 error if it does not exist                       
    contact = Contact.query.get_or_404(id)             
    if request.method == 'POST':
        
        # Grab the user input fields and update them accordingly from the HTML file
        contact.name = request.form['name']            
        contact.phone = request.form['phone']          
        contact.email = request.form['email']
        
        # Commit the changes
        db.session.commit()                            
        return redirect('/')     
    
    # Here we pass contact because                       
    return render_template('edit_contact.html', contact=contact)  

# Delete also has a dynamic URL and this method takes in an ID
@app.route('/delete/<int:id>')  
def delete_contact(id):
    
    # This line gets the contact of the ID or returns a 404 error if it does not exist 
    contact = Contact.query.get_or_404(id)  
    
    # Delete the contact from the database
    db.session.delete(contact)       
    
    # Commit the changes       
    db.session.commit()  
    return redirect('/')                    
    

