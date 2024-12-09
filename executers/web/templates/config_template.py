CONFIG_TEMPLATE = """import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""
