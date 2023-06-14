import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s:%(levelname)s:%(message)s]")

project_name = "IPYRender"

logging.info(f"creating project by name: {project_name}")

#List of files
list_of_files = [
    ".github/worksflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirments.txt",
    "requirments_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filedir,filename = os.path.split(Path(filepath))

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating a directory at :{filedir} for file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0:
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating a  new file {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")
    

