from flask import Flask, jsonify
from models import db, User
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'py_api2',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
db.app = app
admin = User(username = 'admin', email='tarikh@si.co.id')
db.session.add(admin)
db.session.commit()

@app.route("/")
def main():
	admin = User.query.first();
	return jsonify(name = admin.username, email = admin.email)

if __name__ == '__main__':
    app.run()