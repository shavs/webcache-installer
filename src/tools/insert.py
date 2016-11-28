#!/usr/bin/env python3
import fileinput
import os
from html.parser import HTMLParser

# Copy-pasted verbatim from 20.2 html.parser documentation
class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print("Encountered a start tag:", tag)

  def handle_endtag(self, tag):
    print("Encountered an end tag:", tag)

  def handle_data(self, data):
    print("Encountered some data:", data)

parser = MyHTMLParser()

# Insert the file
def insert_html():
    f = open('../index.html', 'r')
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

    line_end -= 1


    n = open('../tools/html.txt', 'r')
    data2 = n.readlines()
    n.close()

    data[line_start:line_end] = data2
    f = open('../index.html','w')
    f.writelines(data)
    f.close()

    print('insert - 0 - ok')

def insert_markdown():
    #!/usr/bin/env python3
    import fileinput
    import os
    import re
    line_start=0
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

    # Current directory
    # print(os.getcwd())


    for root, dirs, files in os.walk(str(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')))):
        for file in files:
            if file.endswith(".md"):
                print('\n\n\n\n')
                # Print the full path, and print the current file name with ext
                # print(os.path.join(root, file))
                print(file)

                # Replace the current file extension name
                filename = str(file.replace('.md', ''))
                # Print the filename without the extension

                # Now, we have to compare the title and the filename.
                for title in titles:
                    if re.match(r'.*<h2>(.*)</h2>', title) != None:
                        line_start = int(titles.index(title)) + 3
                        line_end = line_start + 1
                        # print('\nIt\'s an h2!')
                        # Now we have to remove all the html from the title
                        title = re.sub(r'<[^>]*>', '', title)
                        # Remove all whitespace from either side of the string
                        # there must be a way of concatenating this mess, but for now,
                        # it works.
                        title = title.rstrip()
                        title = title.lstrip()
                        filename = filename.rstrip()
                        filename = filename.lstrip()

                        # If the h2 matches the filename, then...
                        if title == filename:
                            # print('Filename matches!\n' + title + '\nand\n' + filename)
                            # Create the HTML, using the code from earlier...

                            # Open the Markdown file, read it and close it.
                            jarvis = open(os.path.join(root, file))
                            data = jarvis.readlines()
                            jarvis.close()

                            # Create the new array for the HTML DOM to be inserted into
                            html_file_dom = []

                            for line in data:
                                # Strip any line breaks, etc. like \n
                                line = line.rstrip()
                                line = line.lstrip()

                                # Regex matches for the line - one will return true
                                # This could be done so much better than this, but it works for now
                                match = re.search(r'^[#][^#][^#][^#][^#].*', line)
                                match2 = re.search(r'^[#][#][^#][^#][^#].*', line)
                                match3 = re.search(r'^[#][#][#][^#][^#].*', line)
                                match4 = re.search(r'^[#][#][#][#][^#].*', line)
                                match5 = re.search(r'^[#][#][#][#][#].*', line)

                                # If there are any matches...
                                if match:
                                    # Print the line in stdout
                                    # Now substitute the markdown with vaild HTML tags that match
                                    line = re.sub(r'^[#][^#][^#][^#][^#].*', '          <h1>' + line + '</h1>\n', line)
                                    line = line.replace("# ", "")
                                elif match2:
                                    line = re.sub(r'^[#][#][^#][^#][^#].*', '          <h2>' + line + '</h2>\n', line)
                                    line = line.replace("## ", "")
                                elif match3:
                                    line = re.sub(r'^[#][#][#][^#][^#].*', '          <h3>' + line + '</h3>\n', line)
                                    line = line.replace("### ", "")
                                elif match4:
                                    line = re.sub(r'^[#][#][#][#][^#].*', '          <h4>' + line + '</h4>\n', line)
                                    line = line.replace("#### ", "")
                                elif match5:
                                    line = re.sub(r'^[#][#][#][#][#].*', '          <h5>' + line + '</h5>\n', line)
                                    line = line.replace("##### ", "")
                                elif line == '':
                                    #nothing
                                    print('')
                                else:
                                    print('')
                                    line = '          <p>' + line + '</p>\n'
                                # Now append the line to the new HTML DOM that we have to insert
                                html_file_dom.append(line)
                                # Now, the comment needs to be inserted into the document

                            # Print the results of the list
                            print(html_file_dom)
                            titles[line_start:line_end] = html_file_dom

                            index_file = open('../index.html', 'w')
                            index_file.writelines(titles)
                            index_file.close()
                            # Separate out the stdout to make it a little easier to follow
                            print('\n\n\n\n')
                        else:
                            print('')


                            # Now, we need to insert this three lines after the heading was found
