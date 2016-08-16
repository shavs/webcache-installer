#!/bin/bash

# Script to generate a top-level index.html,
# which can then be used to search saved webpages

# This entire file can be rewritten in python, instead of bash.

cd tools/;
#Remove any old links in the page
python3 remove_markdown.py
python3 remove.py

# First, we must find each mention of index.html in files
cd ../websites/;
find `pwd` -regextype sed -regex '.*\.html' | grep -o '[^\.][^\/][A-Z0-9a-z].*' > \
../tools/index_files.txt;
cd ../tools/;
# Now we create the titles by looking through them
touch titles.txt;
rm titles.txt;
for page in `cat index_files.txt | grep -o '.*[A-Z0-9a-z].*' `; do
   grep -oP '(?<=<title>).*(?=</title)' $page >> titles.txt;
done

while true; do
  read -r f1 <&3 || break
  read -r f2 <&4 || break
  echo -e "      <section>\n        <h2>$f1</h2>\n        <a href=\"file:///$f2\">Link</a>\n        <div class=\"comments\">\n\n\n        </div>\n      </section>\n"
done 3<titles.txt 4<index_files.txt >> html.txt
# Can't append in bash using sed as sed is awful and i never want to see it
# again
python3 insert.py
python3 find_markdown.py

# rm html.txt

echo "end"
