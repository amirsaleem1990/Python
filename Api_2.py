# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def index():
# 	return 'Hello'

# @app.route("/drinks")
# def get_drinks():
# 	return {"drinks" : "drinks data"}




# export FLASK_APP=Api_2.py
# export FLASK_ENV=development
# flask run

# firefox http://127.0.0.1:5000/drinks




# ---------------------------------------------------------------
# from flask import Flask
# app = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)


# class Drink(db.Model):
# 	id          = db.Column(db.Integer,   primary_key=True)
# 	name        = db.Column(db.String(80), unique=True, nullable=False)
# 	description = db.Column(db.String(120))

# 	def __repr__(self):
# 		return f"{self.name} - {self.description}"

# @app.route("/")
# def get_drinks():
# 	return {
# 		"drinks" :  [{"name" : drink.name, 'description' : drink.description} for drink in Drink.query.all()]
# 		}


# """
# from Api_2 import db
# from Api_2 import Drink
# db.create_all()
# drink = Drink(name="Grape Soda", description="Tastes like grapes")
# db.session.add(drink)
# db.session.commit()

# db.session.add(Drink(name="cherry", description="Tastes like that one ice cream"))
# db.session.commit()
# # Drink.query.all()"""

# -------------------------------------------------------------------
# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)


# class Drink(db.Model):
# 	id          = db.Column(db.Integer,   primary_key=True)
# 	name        = db.Column(db.String(80), unique=True, nullable=False)
# 	description = db.Column(db.String(120))

# 	def __repr__(self):
# 		return f"{self.name} - {self.description}"

# @app.route("/")
# def get_drinks():
# 	return {
# 		"drinks" :  [{"name" : drink.name, 'description' : drink.description} for drink in Drink.query.all()]
# 		}

# @app.route("/drinks/<id>")
# def get_drink(id):
# 	drink = Drink.query.get_or_404(id)
# 	return {"name" : drink.name, "description" : "drink.description"}


# @app.route("/drinks", methods=['POST'])
# def add_drink():
# 	drink = Drink(
# 		name=request.json['name'], 
# 		description=request.json['description']
# 		)
# 	db.session.add(drink)
# 	db.session.commit()
# 	return {'id' : drink.id}


# @app.route('/drinks/<id>', methods=['DELETE'])
# def deleted_drink(id):
# 	drink = Drink.query.get(id)
# 	if drink is None:
# 		return {"error" : "not found"}
# 	db.session.delete(drink)
# 	db.session.commit()
# 	return {"message" : "yeet!@"}

# """
# from Api_2 import db
# from Api_2 import Drink
# db.create_all()
# drink = Drink(name="Grape Soda", description="Tastes like grapes")
# db.session.add(drink)
# db.session.commit()

# db.session.add(Drink(name="cherry", description="Tastes like that one ice cream"))
# db.session.commit()
# # Drink.query.all()
# """