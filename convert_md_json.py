"""This script is to convert MD files to json structured by separates section
of each paper."""


import os
import re
import json


def get_files(folder_path):
    "Get the path of a folder containing files and return a list of the file names."
    return os.listdir(folder_path)


def extract_main_sections(md_text):
    """Extract main sections from Markdown files with respect to our model structure."""
    pattern = r'^(#+)\s+(.*?)(?=\n#+|\Z)(.*?)(?=\n#+|\Z)'
    
    # extract all sections
    sections = re.findall(pattern, md_text, re.MULTILINE | re.DOTALL)
    
    # Filter out subsections
    main_sections = [(level, title, content) for level, title, content in sections if len(level) == 2 or len(level) == 1]
    
    return main_sections

def separate_content_to_title(tup):
    txt = tup[1].split("\n", 1)
    tup = list(tup)
    tup[1] = txt[0]
    tup[2] = txt[1]
    tup = tuple(tup)

    return tup
    

current_loc = "."
root_folder = "paper_output/"
files = get_files(os.path.join(current_loc, root_folder))

## get the .md files:
md_files =  [file for file in files if file.endswith(".md")]

for file in md_files:
    # open md file
    with open(os.path.join(current_loc, root_folder, file)) as f:
        md_text = f.read()

    # Extract main sections of the current file
    sections = extract_main_sections(md_text)

    #Do a small processing and convert dict to Json
    for i, tup in enumerate(sections):
        sections[i] = separate_content_to_title(tup)
    dict_temp = [{"level": level, "title": title, "content": content} for level, title, content in sections]
    temp_json = json.dumps(dict_temp)

    # Save into json file the structure
    with open(f"paper_sections/{file}_sections.json", "w") as f:
        json.dump(dict_temp, f, indent=4)
        
