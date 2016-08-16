import fileinput
import os

def remove_html():
    # Find the ending line, remove everything between the beginning line and the end
    f = open('../index.html')
    data = f.readlines()
    f.close()
    line_start=0
    line_end=0
    line_count=0

    debug = 0

    start = '      <!-- #GenCode -->\n'
    end = '      <!-- #EndGenCode -->\n'

    for line in data:
        line_count += 1
        if start in line:
            line_start = line_count
        elif end in line:
            line_end = line_count

    # print(line_start)
    # print(line_end)
    # print(line_count)

    line_count = line_start
    # Now we need to remove those lines from the file and rewrite the file
    for line in data:
        line_count += 1
        if line_count == line_end - 1:
            break
        else:
            # debug += 1
            del data[line_start]

    # write to file
    f = open('../index.html','w')
    f.writelines(data)
    f.close()

    print('remove - 0 - ok')

def remove_markdown():
    import fileinput
    import os
    import re
    line_start=0
    line_end = 0
    line_count=0
    # Find all files that have the extension of .md

    # Open the title file - this will contain all the titles that are available
    title_file = open('../index.html', 'r')
    titles = title_file.readlines()
    title_file.close()
    # Now that the titles have been loaded into memory, we can now carry on
    # and load the rest of the files

    # We need to remove the old comments from the file, so that the comments are
    # constantly not the same
    for line in titles:
        line_count += 1
        if re.match(r'.*<div class=\"comments\">(.*)', line) != None:
            line_start = line_count
            print('ls: ' + str(line_start))
        if re.match(r'.*</div>.*', line) != None:
            line_end = line_count - 1
            print('le: ' + str(line_end))
        if (line_end == line_count - 1) and (line_count > 1):
            print('\n')
            # Delete the lines here
            del titles[line_start:line_end]
            # Insert a blank line between the divs,
            titles.insert(line_start, '\n')
            # Open the file and write to it
            title_file = open('../index.html', 'w')
            title_file.writelines(titles)
            title_file.close()
