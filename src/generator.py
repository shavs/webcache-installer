#!/usr/bin/env python3
# Script to generate a top-level index.html file,
# which can then be used to search saved webpages.

# This file is the rewrite of the bash generator.

import sys
import os
import fileinput
import re

# Needed so that index file locations can be stored for inserting into index_files.txt
index_files = []
titles = []
raw_html = []

# First, change the directory to tools
currentdir = os.getcwd()
os.chdir(str(currentdir) + '/tools/')

# sys.path.insert is needed so that we can load modules from tools/
# os.getcwd prints out the current directory without the ending slash
# so we need to add it here.
sys.path.insert(0, str(currentdir) + '/tools/')

# Now we need to import the remove modules, a combo of both
# remove.py and remove_markdown.py
import remove

# Import the insert modules
import insert

# Now that we are in the right dir, we can now run remove.py and remove_markdown.py
remove.remove_markdown()
remove.remove_html()

# Now that we have removed the old HTML and Markdown, it's time to get new content

# First, change to the websites dir
os.chdir(str(currentdir) + '/websites/')
for root, dirs, files in os.walk(str(os.path.abspath(os.path.join(os.path.dirname(__file__), '', '')))):
    for file in files:
      # Now if the file ends in HTML
        if file.endswith(".html"):
          # Print out a result for debug
          # print('Found a file: ' + str(root) + '/' + str(file))
          # Now that the file has been found, we need to append it to an array
          # / list for use later in writing to html.txt
          #
          # Also, str is used to make sure the type is right
          index_files.append(str(root) + str(file) + '\n')
          # Now that we have the file, we might as well look for the title tag
          # too, whilst we still have the whole file path
          html_index_file_read = open(os.path.join(root, file))
          html_index_file_data = html_index_file_read.readlines()
          html_index_file_read.close()
          # Now that we have the contents of the file, we need to read it line
          # by line so that the HTML file is fully read.
          for line in html_index_file_data:
            # strip any whitespace from either side of the line
            line = line.rstrip()
            line = line.lstrip()
            # Now that the whitespace has been removed, using regex...
            title_match = re.search(r'(?<=<title>).*(?=</title)', line)

            # If the line matches...
            if title_match:

              # Remove the title beginning tag
              line = line.replace("<title>", "")

              # Remove the ending title tag
              line = line.replace("</title>", "")

              # Remove the special character /

              title_match_special = re.search(r'[/].*', line)

              # if there is a match:
              if title_match_special:
                  line = line.replace("/", "")

              # Now we have the raw content, we are now gonna add the two other tags
              line = '        <h2>' + line + '</h2>\n'

              # Add the title to the list
              titles.append(line)

              # Create the html lines
              full_lines = '      <section>\n' + line + \
              '        <a href=\"file:///' + str(root) + '/' + str(file) + \
              '\">Link</a>\n        <div class=\"comments\">\n\n\n        </div>\n      </section>\n'

              raw_html.append(full_lines)

# Change the directory back to /tools/
os.chdir(str(currentdir) + '/tools/')

# At the end, write to index_files.txt
html_index_file = open('index_files.txt', 'w')
html_index_file.writelines(index_files)
html_index_file.close()

# Write the titles to the file
title_file = open('titles.txt', 'w')
title_file.writelines(titles)
title_file.close()

# Create the raw html file for writing
raw_html_file = open('html.txt', 'w')
raw_html_file.writelines(raw_html)
raw_html_file.close()

# Next, we need to run the insert and markdown_insert modules
insert.insert_html()
insert.insert_markdown()

# end of python file
