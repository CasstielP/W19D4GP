from flask import Blueprint, redirect, render_template, url_for




bp = Blueprint("pokemon", __name__, url_prefix="/api")



@bp.route('/pokemon')
def get_all_pokemon():
    return '<h1>testing2</h1>'
