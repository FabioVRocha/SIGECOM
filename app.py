from flask import Flask, render_template
from backend.config import Config
from dotenv import load_dotenv

from backend.extensions import db
from backend.models import Cliente


load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from backend.cadastros.routes import cadastros_bp
    from backend.estoque.routes import estoque_bp
    from backend.vendas.routes import vendas_bp

    app.register_blueprint(cadastros_bp)
    app.register_blueprint(estoque_bp)
    app.register_blueprint(vendas_bp)

    @app.route('/')
    def index():
        clientes = Cliente.query.all()
        return render_template('index.html', clientes=clientes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)