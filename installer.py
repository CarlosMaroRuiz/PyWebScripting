from InquirerPy import inquirer
from colorama import Fore, Style, init
import os

from executers.rest_fast.execute import install_rest_fast
from executers.web.execute import install_web_flask
from utils.create_virtualenv import create_virtualenv

init(autoreset=True)

def show_banner():
    print(Fore.GREEN + """
   __        __   _     ____         
   \ \      / /__| |__ |  _ \ _   _ 
    \ \ /\ / / _ \ '_ \| |_) | | | |
     \ V  V /  __/ |_) |  __/| |_| |
      \_/\_/ \___|_.__/|_|    \__, |
                              |___/ 
    """ + Fore.YELLOW + """
    pyWeb: Project Creator for Web Development using layered style
    """ + Fore.WHITE + """
    Version: 1.0
    Codename: pyWeb
    Follow me on GitHub: @CarlosMaroRuiz
    """)

def ask_project_folder():
    project_folder = inquirer.text(
        message="Enter the name of the folder where the project will be created:",
        validate=lambda x: len(x.strip()) > 0 or "Folder name cannot be empty."
    ).execute()

    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
        print(Fore.GREEN + f"Folder '{project_folder}' created successfully!")
    else:
        print(Fore.YELLOW + f"Folder '{project_folder}' already exists.")

    return project_folder

def main():
    show_banner()

    options = [
        "CREATE WEB PROJECT WITH FLASK, JINJA, TAILWIND and MySql",
        "CREATE API REST WITH FASTAPI and MySql",
        "CREATE API REST WITH FLASK-RESTFUL and MySql",
        "EXIT"
    ]

    choice = inquirer.select(
        message="SELECT AN OPTION TO BEGIN:",
        choices=options,
        default="EXIT",
        multiselect=False,
        instruction="Use the ↑/↓ keys to navigate and Enter to select"
    ).execute()

    print(Fore.CYAN + f"You selected: {choice}")

    if choice == "EXIT":
        print(Fore.RED + "Exiting the program. Goodbye!")
        return

    project_folder = ask_project_folder()

    if choice == "CREATE WEB PROJECT WITH FLASK, JINJA, TAILWIND and MySql":
        print(Fore.GREEN + f"Creating a web project with Flask, Jinja, and Tailwind in '{project_folder}'...")
        install_web_flask(project_folder)
    elif choice == "CREATE API REST WITH FASTAPI and MySql":
        print(Fore.GREEN + f"Creating an API REST with FastAPI in '{project_folder}'...")
        install_rest_fast(project_folder)
    elif choice == "CREATE API REST WITH FLASK-RESTFUL and MySql":
        print(Fore.YELLOW + "This feature is currently under development.")
        print(Fore.GREEN + f"Preparing the structure for Flask-RESTful in '{project_folder}'...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting the program. Goodbye!")
