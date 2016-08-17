#!/usr/bin/env python3

# Installer file for webcache
# Should allow a target directory and also a custom name for downloading files
import os
import fileinput
import shutil
custom_bash_downloader_data = []
# First, we need the name of the place to install it
#file_name = input('What is going to be the name of the file? ')
# file_name can go in place of /webcache/, if need be.

# Next, we need the directory where it is going to be installed to

path = str(input('What is the path that webcache is going to be installed to?' +
'\nNote, this has to be the full path.\n'))

# If the user enters `directory//`, the shell is nice enough to understand what
# they meant by that and can be used without error.

current_location = str(os.getcwd())
shutil.copytree(current_location + '/src/', path + '/webcache/')

# After this, we now have to find somewhere to install this file to, so that the
# file can be run and that we are all happy.

# First of all, we have to change the name of the downloader script and copy it
# to /usr/bin
os.chdir(path + '/webcache/')

# Now that we are in the right dir, we need to change the bash script

# change the path that the websites directory currently lies in
bash_downloader = open('scripts/download-webpage.sh', 'r')
bash_downloader_data = bash_downloader.readlines()
bash_downloader.close()

line_to_replace='websites='

for line in bash_downloader_data:
    # remove any whitespace from the line either side of any content
    line.rstrip()
    line.lstrip()
    # If the line exists in the file, then we write to it
    if line_to_replace in line:
        # Replace the websites path with a real path
        line = 'websites=\"' + path + '/webcache/websites/\"\n'
    # Append the new data to a list
    custom_bash_downloader_data.append(line)

# Now we have to write out the new file
new_bash_file = open('scripts/download-webpage.sh', 'w')
new_bash_file.writelines(custom_bash_downloader_data)
new_bash_file.close()

# Now we need to rename the script to the right name, then leave it
# up to the user to copy the shell file to /usr/bin.
download_name = str(input('What name you would like to give to the downloader?\n'))
os.rename('scripts/download-webpage.sh', 'scripts/download-webpage-' + download_name)


print('\n\n\nCopied to ' + path + '. Have fun!')
print('\nNote - you may need to reload the terminal that you are using' + \
' in order to take advantage of the new download command.')
print('\nCopy the script file in \'webcache/scripts/\' ' + \
'to /usr/bin in order to download webpages.')
