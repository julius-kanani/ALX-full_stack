from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect to a database by setting a configuration variable
# set on the dictionary app.config
# SQLALCHEMY_DATABASE_URI configuration variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2135@localhost:5432/alx_web'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instance of a database that we can interact with
db = SQLAlchemy(app)

# person model
class Person(db.Model):
	__tablename__ = 'people'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)

	# wrapper
	def __repr__(self):
		return f'<Person ID: {self.id}, name: {self.name}>'

# create the table people
db.create_all()

@app.route('/')
def hello():
	person = Person.query.first();
	return f'Hello, ' + person.name

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0")
