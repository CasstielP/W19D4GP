from flask import Blueprint, redirect, render_template, jsonify
from app.models import db, Pokemon, Item, Type
import json



bp = Blueprint("pokemon", __name__, url_prefix="/api")



@bp.route('/pokemon')
def get_all_pokemon():
    all_pokemon = Pokemon.query.all()

    all = []
    for pok in all_pokemon:
        all.append({
        "imageUrl": pok.image_url,
        "id": pok.id,
        "number": pok.number,
        "name": pok.name,
        "captured": pok.captured
    })

    return jsonify(all)
