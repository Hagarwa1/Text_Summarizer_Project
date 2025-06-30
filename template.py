import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name= 'textSummarizer'

# creating folders and files and providing path to them 

list_of_files= ['.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    ]

for filepath in list_of_files:
    # using Path function to help understand the correct path to the folders described in above file list based on windows or linux, thus handles path issue
    
    filepath = Path(filepath)

    #the above file list has the location of the new files & folders, now we need to split them into directory & name
    filedir, filename = os.path.split(filepath)

    #checking if directory is made or not and showing a message 
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #similar to mkdir command if directory not made, then make it
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    #checking if file is made or not and show a message
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if file does not exist or has size = 0
        with open(filepath, 'w') as f: # then craete the file
            pass
            logging.info(f"Creating empty file: {filepath}") # show message

    else:
        logging.info(f"{filename} already exists") # else give this message
