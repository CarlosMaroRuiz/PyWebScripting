INDEX_CONTROLLER_TEMPLATE = """from flask import Blueprint, render_template

index_bp = Blueprint("index", __name__)

# Ruta para la página de inicio
@index_bp.route("/")
def home():
    return render_template("index.html")
"""