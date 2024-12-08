import re

def read_input():
    with open('input.txt', 'r') as file:
        return file.read().splitlines()

lines = read_input()

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', ' '.join(lines))
matches2 = re.findall(r'(do\(\)|don\'t\(\))*(.*?)?mul\((\d{1,3}),(\d{1,3})\)', ' '.join(lines))

# Part 1.
print(sum(int(match[0]) * int(match[1]) for match in matches))

# Part 2.
do = True
s = 0
for match in matches2:
    for j in match:
        if 'do()' in j:
            do = True
        elif "don't()" in j:
            do = False
    if do:
        s += int(match[-1]) * int(match[-2])

print(s)