from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)


db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

# Ensure the required tables exist when the application starts
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('index.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)