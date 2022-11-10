from flask import Flask, render_template, redirect
# import statement for CSRF
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from app.config import Configuration
from .models import db, Item, Pokemon
from .routes import pokemon
import os

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon.bp)
db.init_app(app)
Migrate(app, db)





# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response



@app.route("/")
def index():
    return '<h1>testing</h1>'
