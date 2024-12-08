def get_dependencies():
    dependencies = [
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "pydantic",
        "pydantic[email]",
        "passlib[bcrypt]",
        "python-dotenv",
        "pymysql",
        "python-jose",
        "requests"

    ]
    return dependencies
