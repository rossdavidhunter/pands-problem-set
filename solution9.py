# Solution 9
# use of open() to return file object in path below
with open("C:\\Users\\hunterd\\Desktop\\Moby Dick\\moby-dick.txt", "r") as f:

    lines = f.readlines()

desired_lines = [x.strip() for x in lines[1::2]]

print(desired_lines)
