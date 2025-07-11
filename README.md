# SIGECOM Backend

This repository contains a minimal Flask application with SQLAlchemy.
Recent updates introduced skeleton modules covering the main areas of the
SIGECOM system such as cadastros, estoque, vendas, compras, financeiro,
relatórios e configurações. Each module defines basic SQLAlchemy models that
can be expanded in the future.

## Configuration

Database settings are configured in `backend/config.py`. By default the application
connects to a PostgreSQL database named `sigecom_db` on `localhost` using the
user `user` and password `password`. You can override this by setting the
`DATABASE_URL` environment variable using the standard PostgreSQL connection
string syntax, e.g.

```
export DATABASE_URL=postgresql://myuser:mypass@localhost:5432/sigecom_db
```

## Running

Install the dependencies and run the application:

```
pip install -r backend/requirements.txt
python backend/app.py
```