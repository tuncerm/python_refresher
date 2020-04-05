from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'


db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name


if __name__ == '__main__':
    app.run()

#
#   req.args.get('field')   // query params
#   req.form.get('field')   // form data
#   req.data   // json data --> json.loads(req.data) === returns a data dictionary
#
# >>> Person.query.all()
# >>> Person.query.first()
# >>> query = Person.query.filter(Person.name == 'Amy')
# >>> query.first()
# >>> query.all()
#
# person = Person(name='Amy')
# db.session.add(person)        add_all([array])
# db.session.commit()

# Flask-SQLAlchemy Data Types
# Integer
# String(size)
# Text
# DateTime
# Float
# Boolean
# PickleType
# LargeBinary

# SQLAlchemy Constrains
# nullable
# unique
#
# Example
# name = db.Column(db.String(), nullable=False, unique=True)
#
# Implementing a check constraint
# price = db.Column(db.Float, db.CheckConstraint('price>0'))
#
