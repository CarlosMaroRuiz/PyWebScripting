USER_SERVICE_TEMPLATE = """from app.repositories.user_repository import get_user_by_id, get_all_users, create_user

def list_all_users():
    users = get_all_users()
    return {
        "total_users": len(users),
        "users": [{"id": user.id, "username": user.username} for user in users]
    }

def register_new_user(username, email, password):
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")

    existing_user = next((u for u in get_all_users() if u.email == email), None)
    if existing_user:
        raise ValueError("El email ya está registrado.")
    return create_user(username=username, email=email, password_hash=password)

def get_user_details(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return None

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }
"""
