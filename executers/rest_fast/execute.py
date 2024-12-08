from executers.rest_fast.create_project_structure import create_project_structure
from executers.rest_fast.dependes import get_dependencies
from utils.create_virtualenv import create_virtualenv
from utils.install_depends import install_dependencies

def install_rest_fast(path_folder):
    create_virtualenv(path_folder)
    dependencies = get_dependencies()
    install_dependencies(path_folder, dependencies)
    create_project_structure(path_folder)