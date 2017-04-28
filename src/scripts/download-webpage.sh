#!/bin/bash

# Script to download webpages and archive them using wget

# THIS IS A LINE TO BE DELETED BY PROGRAM

# which hasn't been created yet.

# Clear to get rid of everything before
clear;

# Now we need a directory name and also the name of the archive, this
# will be used as both
echo -e "Please enter archive and folder name: "
read webarc
# Just makes sure that the variable is set to something that would be useful
# echo -e "Website given: $1"

# We need the original directory that this was triggered in, and also
# the directory of the websites path
# e.g. currentdir -> websites -> newdir -> currentdir
currentdir=$(pwd)

# This line is changed for the variable `websites`
# By default, this will be inoperable as it assigns nothing, and therefore
# commands like mkdir and others will break.

websites=

# Now we echo out these as a test (not really needed any more, just for testing)
# echo -e "Variable set to $webarc \n"
# echo -e "Currentdir: $currentdir";
# echo -e "Websites location: $websites";
# echo -e "Current URL input: $1"

cd "$websites";
mkdir "$webarc";
cd "$webarc";
# Now we do the actual downloading.
wget --convert-links --warc-file="$webarc" \
     --adjust-extension --page-requisites --no-parent --no-verbose --wait=1 \
     --user-agent=Mozilla --span-hosts "$1"

# Before we move out of this, we might as well store the original
# URL inside of the folder, as it may be of some use later on.

echo "$1" > "original_url.txt";

# After this has been done, we are then going to change
# back to the original directory
cd "$currentdir";
echo -e "\n"
echo "Done. Thanks! Remember to run ./generator.py again."
echo -e "\n"
