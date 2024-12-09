import os
import subprocess


def execute_npm_commands(base_path):

    try:
        os.chdir(base_path)
        print("Initializing package.json...")
        subprocess.run(["npm", "init", "-y"], check=True)
        print("Installing TailwindCSS and dependencies...")
        subprocess.run(["npm", "install", "-D", "tailwindcss", "postcss", "autoprefixer"], check=True)
        print("Initializing TailwindCSS configuration...")
        subprocess.run(["npx", "tailwindcss", "init"], check=True)
        print("npm setup completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing npm commands: {e}")
    except FileNotFoundError:
        print("npm is not installed or not found in the system PATH.")