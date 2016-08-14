#!/usr/bin/env python3
import fileinput
import os

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
