import os

def get_lines(path_files):
    f = open(path_files, "r", encoding="utf-8")
    # open(filename, encoding="utf8")
    lines = f.readlines()
    return lines

# print(get_lines(path_files))

def get_component_info(path_intermediate, Component, all_lines):
    # all_lines = get_lines(path_files=path_files)
    first_line = all_lines[0]
    with open(path_intermediate, 'w', encoding="utf-8") as outfile:
        copy = False
        for line in all_lines:
            if f"Initial {Component}" in line:
                outfile.write(line.replace("  ", ";"))
                copy = True
                continue
            elif first_line in line:
                copy = False
                continue
            elif copy:
                outfile.write(line.replace("  ", ";"))
    return None

def process_file(path_files):
    # path_files = os.path.join("./input/text_file.txt")
    all_lines = get_lines(path_files=path_files)
    path_intermediate = ".\\output\\text_file.txt"
    get_component_info(path_intermediate=path_intermediate, 
                       Component="Hardware", all_lines=all_lines)
    
    return "text_file.txt"


# get_component_info(path_intermediate=path_intermediate, Component="Hardware")