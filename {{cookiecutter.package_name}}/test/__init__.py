import sys
import os

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
mypkg_path= os.path.join(project_path, '{{cookiecutter.package_name}}')
sys.path.append(mypkg_path)
