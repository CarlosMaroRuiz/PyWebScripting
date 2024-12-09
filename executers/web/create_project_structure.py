import os

from executers.web.templates.directive_template import DIRECTIVE_TEMPLATE_TAILWIND
from executers.web.templates.index_html_template import INDEX_HTML_TEMPLATE
from executers.web.execute_npm_commands import execute_npm_commands
from executers.web.templates.index_controller_template import INDEX_CONTROLLER_TEMPLATE
from executers.web.templates.init_template import INIT_TEMPLATE
from executers.web.templates.user_controller_template import USER_CONTROLLER_TEMPLATE
from executers.web.templates.user_model_template import USER_MODEL_TEMPLATE
from executers.web.templates.user_repository_template import USER_REPOSITORY_TEMPLATE
from executers.web.templates.user_service_template import USER_SERVICE_TEMPLATE
from executers.web.templates.config_template import CONFIG_TEMPLATE
from executers.web.templates.run_template import RUN_TEMPLATE
from utils.create_tailwind_config import  create_or_edit_tailwind_config
def create_web_project_structure(base_path):
    structure = {
        "app": {
            "__init__.py": INIT_TEMPLATE,
            "controllers": {
                "__init__.py": "",
                "index_controller.py": INDEX_CONTROLLER_TEMPLATE,
                "user_controller.py": USER_CONTROLLER_TEMPLATE
            },
            "models": {
                "__init__.py": "",
                "user.py": USER_MODEL_TEMPLATE
            },
            "repositories": {
                "__init__.py": "",
                "user_repository.py": USER_REPOSITORY_TEMPLATE
            },
            "services": {
                "__init__.py": "",
                "user_service.py": USER_SERVICE_TEMPLATE
            },
            "utils": {},
            "views": {
                "__init__.py": "",
                "templates": {},  # Templates directory created here
                "static": {
                    "styles.css": ""
                }
            }
        },
        "frontend/src": {
            "styles.css": DIRECTIVE_TEMPLATE_TAILWIND
        },
        "node_modules": None
    }

    for folder, subfolders in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder created: {folder_path}")

        if isinstance(subfolders, dict):
            for subfolder_or_file, content in subfolders.items():
                subfolder_or_file_path = os.path.join(folder_path, subfolder_or_file)
                if isinstance(content, str):
                    with open(subfolder_or_file_path, "w") as f:
                        f.write(content)
                    print(f"File created: {subfolder_or_file_path}")
                elif isinstance(content, dict):
                    os.makedirs(subfolder_or_file_path, exist_ok=True)
                    print(f"Subfolder created: {subfolder_or_file_path}")

                    for subfile, subcontent in content.items():
                        subfile_path = os.path.join(subfolder_or_file_path, subfile)
                        if isinstance(subcontent, str):
                            with open(subfile_path, "w") as f:
                                f.write(subcontent)
                            print(f"File created: {subfile_path}")
                        else:
                            print(f"Error: Unsupported content type for {subfile_path}: {type(subcontent)}")

    #
    templates_path = os.path.join(base_path, "app", "views", "templates")
    os.makedirs(templates_path, exist_ok=True)
    index_html_path = os.path.join(templates_path, "index.html")

    if not os.path.exists(index_html_path):
        with open(index_html_path, "w") as f:
            f.write(INDEX_HTML_TEMPLATE)
        print(f"File created: {index_html_path}")
    else:
        print(f"File already exists: {index_html_path}")

    base_files = {
        "app/config.py": CONFIG_TEMPLATE,
        ".env": """# Environment variables
DATABASE_URL=mysql+pymysql://user:password@localhost/my_database
SECRET_KEY=your_secret_key
""",
        "run.py": RUN_TEMPLATE
    }

    for file, content in base_files.items():
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)
            print(f"File created: {file_path}")
        else:
            print(f"File already exists: {file_path}")

    execute_npm_commands(base_path)
