import os


def create_or_edit_tailwind_config():
    current_path = os.getcwd()


    file_path = os.path.join(current_path, "tailwind.config.js")

    tailwind_config_content = f"""/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  content: ["./app/views/templates/**/*.html", "./frontend/src/**/*.css"],
  theme: {{
    extend: {{}},
  }},
  plugins: [],
}}
"""
    with open(file_path, "w") as f:
        f.write(tailwind_config_content)
    print(f"Overwritten Tailwind CSS config file: {file_path}")
