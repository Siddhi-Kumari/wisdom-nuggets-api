from flask import Blueprint, request, jsonify
from .model import WisdomNugget
from .database import db
import random

nuggets_bp = Blueprint('nuggets', __name__)

@nuggets_bp.route('/nuggets', methods=['GET'])
def get_all_nuggets():
    nuggets = WisdomNugget.query.all()
    return jsonify([n.to_dict() for n in nuggets]), 200

@nuggets_bp.route('/nuggets/random', methods=['GET'])
def get_random_nugget():
    nuggets = WisdomNugget.query.all()
    if not nuggets:
        return jsonify({"error": "No nuggets found"}), 404
    return jsonify(random.choice(nuggets).to_dict()), 200

@nuggets_bp.route('/nuggets', methods=['POST'])
def create_nugget():
    data = request.get_json()
    if not data or 'text' not in data or 'author' not in data:
        return jsonify({"error": "Missing text or author"}), 400
    nugget = WisdomNugget(text=data['text'], author=data['author'])
    db.session.add(nugget)
    db.session.commit()
    return jsonify(nugget.to_dict()), 201

@nuggets_bp.route('/nuggets/<int:nugget_id>', methods=['DELETE'])
def delete_nugget(nugget_id):
    nugget = WisdomNugget.query.get(nugget_id)
    if not nugget:
        return jsonify({"error": "Nugget not found"}), 404
    db.session.delete(nugget)
    db.session.commit()
    return jsonify({"message": "Nugget deleted"}), 200
