from flask_sqlalchemy import SQLAlchemy

# initialize the database as an object of SQlAlchemy
db = SQLAlchemy()


# Create a new contact class, taking in the database model as a parameter
class Contact(db.Model):
    
    # assign an ID in the system, making it the primary key and an int
    id = db.Column(db.Integer, primary_key=True)
    
    # assign a name, phone, and email strng with certain amount of characters and 
    # make sure that the column cannot contain NULL values
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    