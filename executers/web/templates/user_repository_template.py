USER_REPOSITORY_TEMPLATE = """from app.models.user import User
from app import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(username, email, password_hash):
    new_user = User(username=username, email=email)
    new_user.set_password(password_hash)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
"""
