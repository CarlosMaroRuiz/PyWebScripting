
import subprocess
from executers.web.create_project_structure import create_web_project_structure
from utils.create_tailwind_config import create_or_edit_tailwind_config
from utils.create_virtualenv import create_virtualenv
from executers.web.dependes import get_dependencies
from utils.install_depends import install_dependencies


def install_web_flask(path_folder):
    create_virtualenv(path_folder)
    dependencies = get_dependencies()
    install_dependencies(path_folder, dependencies)
    create_web_project_structure(path_folder)
    create_or_edit_tailwind_config()

    try:
        print("[INFO] Running TailwindCSS build process...")
        subprocess.run(
            [
                "npx", "tailwindcss",
                "-i", "./frontend/src/styles.css",
                "-o", "./app/views/static/styles.css",
                "--minify"
            ],
            check=True
        )
        print("[SUCCESS] TailwindCSS styles built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to build TailwindCSS styles: {e}")

