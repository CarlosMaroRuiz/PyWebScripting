import os
import subprocess
import sys

def install_dependencies(path_folder, dependencies):
    pip_path = os.path.join(
        path_folder, "venv", "bin", "pip"
    ) if sys.platform != "win32" else os.path.join(
        path_folder, "venv", "Scripts", "pip.exe"
    )

    if not os.path.exists(pip_path):
        raise FileNotFoundError(f"No se encontró pip en la ruta: {pip_path}. Verifica que el entorno virtual se haya creado correctamente.")

    requirements_path = os.path.join(path_folder, "requirements.txt")

    with open(requirements_path, "w") as f:
        f.write("\n".join(dependencies))
    print(f"Archivo requirements.txt creado en '{requirements_path}'.")

    print("Instalando dependencias...")
    for dependency in dependencies:
        subprocess.run([pip_path, "install", dependency], check=True)
    print("Dependencias instaladas correctamente.")
