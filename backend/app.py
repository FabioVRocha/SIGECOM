from flask import Flask, render_template
from config import Config
from dotenv import load_dotenv

from .extensions import db
from .modules.cadastros import Cliente

load_dotenv()

app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)

db.init_app(app)

# Ensure the required tables exist when the application starts
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('index.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)