import os
from pathlib import Path

project_source_name='src/cnnClassifier'

Files_Folder_list=[
    ".github/workflows/.gitkeep"
    f"{project_source_name}/__init__.py",
    f"{project_source_name}/components/__init__.py",
    f"{project_source_name}/config/__init__.py",
    f"{project_source_name}/config/configuration.py",
    f"{project_source_name}/constants/__init__.py",
    f"{project_source_name}/entity/__init__.py",
    f"{project_source_name}/pipline/__init__.py",
    f"{project_source_name}/utils/__init__.py",
    "research/trials.ipynb",
    "config/config.yaml",
    "dvc.yaml"
    "requirements.txt",
    "params.yaml",
    "setup.py",
    "templates/index.html"]


for filepath in Files_Folder_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")