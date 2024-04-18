"""This script is a temporary script for converting many Pdfs to 
markdown using Marker sequentially."""


import os
import subprocess
import sys

def get_files(folder_path):
    "Get the path of a folder containing pdfs and return a list of the file names."
    return os.listdir(folder_path)

current_loc = "."
root_folder = "papers/"
pdfs = get_files(f"{current_loc}/{root_folder}")

# running Marker for each pdf 
# activate virtual environment:
poetry_activate_cmd = f"cd {current_loc}/markerx/ && poetry shell"
subprocess.Popen(poetry_activate_cmd, shell=True).wait()

# Convert pdfs into markdown in the output_papers folder.
for i in range(len(pdfs)):
    command = f"cd ./markerx/ && {sys.executable} ./convert_single.py ../{root_folder}/{pdfs[i]} ../paper_output/output_{i}.md --parallel_factor 2"
    subprocess.Popen(command, shell=True).wait()

