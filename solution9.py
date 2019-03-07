# Ross Hunter, 2019 Solution 9 secondstring

# Adapted from: https://stackabuse.com/read-a-file-line-by-line-in-python/ and Lecture 7 'Open Files for Reading and Writing'

# use of open() to return file object in path below
with open("C:\\Users\\hunterd\\Desktop\\Moby Dick\\moby-dick.txt", "r") as f:

# readlines will read all lines of text
    lines = f.readlines()

# use of strip() removes space between lines
    desired_lines = [x.strip() for x in lines[1::2]]

print(desired_lines)

