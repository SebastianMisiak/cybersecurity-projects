with open("passwords.txt", "r") as f:
    lines = f.readlines()

line_count = 0

for line in lines:
    print(line.strip())
    line_count += 1

if line_count == 0:
    print(f"The file is empty")
elif line_count == 1:
    print(f"There is {line_count} line in the file.")
else:
    print(f"There are {line_count} lines in the file.")