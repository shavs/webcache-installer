#!/usr/bin/env python3
import fileinput
import os
# Insert the file

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
