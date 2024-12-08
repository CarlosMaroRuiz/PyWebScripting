import os
from .templates.security_hash_template import SECURITY_HASH_TEMPLATE
from .templates.decoder_token_template import DECODER_TOKEN_TEMPLATE
from .templates.bd_config_template import CONFIG_TEMPLATE
from .templates.bd_session_template import SESSION_TEMPLATE
from .templates.bd_models_base_template import BASE_TEMPLATE
from .templates.auth_generate_token_template import GENERATE_TOKEN_TEMPLATE
from .templates.middleware_rate_limiter_template import RATE_LIMITER_TEMPLATE
from .templates.main_template import MAIN_TEMPLATE


def create_project_structure(base_path):
    structure = {
        "api": [],
        "auth": ["__init__.py", "decoderToken.py", "generateToken.py"],
        "bd": ["__init__.py", "config.py", "session.py"],
        "middleware": ["rate_limiter_middleware.py"],
        "schemas": [],
        "services": [],
        "utils": ["securityHash.py"]
    }

    subfolders = {
        "bd": {"models": ["base.py"]}
    }

    file_contents = {
        "utils/securityHash.py": SECURITY_HASH_TEMPLATE,
        "auth/decoderToken.py": DECODER_TOKEN_TEMPLATE,
        "auth/generateToken.py": GENERATE_TOKEN_TEMPLATE,
        "bd/config.py": CONFIG_TEMPLATE,
        "bd/session.py": SESSION_TEMPLATE,
        "bd/models/base.py": BASE_TEMPLATE,
        "middleware/rate_limiter_middleware.py": RATE_LIMITER_TEMPLATE,
        "main.py": MAIN_TEMPLATE
    }


    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder created: {folder_path}")

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    content = file_contents.get(os.path.relpath(file_path, base_path), "")
                    f.write(content)
                print(f"File created: {file_path}")
            else:
                print(f"File already exists: {file_path}")


    for folder, subfolder_dict in subfolders.items():
        folder_path = os.path.join(base_path, folder)
        for subfolder, subfolder_files in subfolder_dict.items():
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"Subfolder created: {subfolder_path}")

            for subfile in subfolder_files:
                subfile_path = os.path.join(subfolder_path, subfile)
                if not os.path.exists(subfile_path):
                    with open(subfile_path, "w") as f:
                        content = file_contents.get(os.path.relpath(subfile_path, base_path), "")
                        f.write(content)
                    print(f"File created: {subfile_path}")
                else:
                    print(f"File already exists: {subfile_path}")

    env_file_path = os.path.join(base_path, ".env")
    if not os.path.exists(env_file_path):
        with open(env_file_path, "w") as f:
            f.write("""# General application configuration
SecretKey=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database configuration
DATABASE_URL=sqlite:///./test.db

# Rate limiter middleware configuration
RATE_LIMIT_MAX_REQUESTS=5
RATE_LIMIT_PERIOD=60
""")
        print(f".env file created: {env_file_path}")
    else:
        print(f".env file already exists: {env_file_path}")


    base_files = ["main.py", ".gitignore"]
    for file in base_files:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                content = file_contents.get(os.path.relpath(file_path, base_path), "")
                f.write(content)
            print(f"File created: {file_path}")
        else:
            print(f"File already exists: {file_path}")


if __name__ == "__main__":
    BASE_PATH = "my_project"
    os.makedirs(BASE_PATH, exist_ok=True)
    print(f"Base folder created: {BASE_PATH}")

    create_project_structure(BASE_PATH)
