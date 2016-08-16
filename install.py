#!/usr/bin/env python3

# Installer file for webcache
# Should allow a target directory and also a custom name for downloading files
import os
import fileinput
import shutil

# First, we need the name of the place to install it
#file_name = input('What is going to be the name of the file? ')
# file_name can go in place of /webcache/, if need be.

# Next, we need the directory where it is going to be installed to

path = input('What is the path that webcache is going to be installed to? ')

# After this, we now have to find somewhere to install this file to, so that the
# file can be run and that we are all happy.
current_location = str(os.getcwd())
shutil.copytree(current_location + '/src/', str(path) + '/webcache/')
print('Copied to ' + path + '. Have fun!')
