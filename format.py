import sys
import shutil
from distutils.dir_util import copy_tree
import os
import re

def addBlockSign(string):
    # $$ something $$ -> $$\\[ something \\] \n $$
    pattern = r'\$\$'
    segments = re.split(pattern, string)
    newSegments=[]

    for i in range(0, len(segments)-1):
        insert="$$\\\\["
        if(i%2==1):
            insert="\\\\]\n$$"
        newSegments.append(segments[i])
        newSegments.append(insert)
    return ''.join(newSegments)

def list_files(directory):
    file_paths = []  # List to store the file paths

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)
    return file_paths
def convert_markdown_to_html(markdown_text):
    # Convert Markdown image syntax: ![](url) to <image src="url" width="80">
    image_pattern = r'!\[.*?\]\((.*?)\)'
    html_text = re.sub(image_pattern, r'<image src="\1" width="80%">\n', markdown_text)

    # Convert * label: something to * **label**: something
    label_pattern = r'\* (?: {0,2})(?!\*\*|<|\[)(.*?)(?: {0,2})(:) *(.*?)\n'
    html_text = re.sub(label_pattern,r'* **\1**\2 \3 \n', html_text)
    return html_text
def processMarkdown(path,final_path):
    with open(path,"r") as f:
        text=f.read()

        # remap=[("\\\\"," \\\\\\\\"),
        #        ("\\{"," \\\\{ "),
        #        ("\\}"," \\\\} "),
        #        ("*"," \\times ")]
        # for target,value in remap:
        #     text=text.replace(target,value)
        process_text=convert_markdown_to_html(text)
        with open(final_path,"w") as f2:
            f2.write(process_text)


if __name__=="__main__":
    source_dir=sys.argv[1]
    write_dir=sys.argv[2]

    try:
        copy_tree(source_dir, write_dir)
        # shutil.copytree(path,writePath,copy_function=shutil.copy2)
    except FileExistsError:
        print("existed")
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, source_dir)
            destination_file_path = os.path.join(write_dir, relative_path)
            # shutil.copy2(file_path, destination_file_path)
            if(".md" in file_name):
                processMarkdown(file_path,destination_file_path)
