USER_CONTROLLER_TEMPLATE = """from flask import Blueprint, request, jsonify
from app.services.user_service import list_all_users, register_new_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = list_all_users()
    return jsonify(users)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = register_new_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return jsonify({"message": "Usuario creado con éxito", "user": new_user.username}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
"""
