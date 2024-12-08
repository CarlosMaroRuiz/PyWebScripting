import os
import subprocess
import sys


def create_virtualenv(project_path):

    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], cwd=project_path)
    print("Entorno virtual creado.")
