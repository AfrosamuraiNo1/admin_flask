from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['FLASK_ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'alfw;fjw[fkpwefk[eefk[15434675690595250fke'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@app.get('/')
def index():
    return render_template('index.html')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    info = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f'Place: {self.name}{self.info}{self.address}{self.description}{self.latitude}{self.longitude}'

admin = Admin(app, name="My blog", template_mode="bootstrap3")
admin.add_view(ModelView(User, db.session, name='Пользователь'))
admin.add_view(ModelView(Place, db.session, name='Ресторан'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
