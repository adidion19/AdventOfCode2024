def read_input():
    with open('input.txt', 'r') as file:
        return file.read().splitlines()

lines = read_input()
parsed_line = {line.split()[0] : line.split()[1] for line in lines}
left = parsed_line.keys()
right = parsed_line.values()



# Part 1.
# print(sum([abs(int(l) - int(r)) for l, r in zip(sorted(left), sorted(right))]))

# Part 2.
print(sum([list(right).count(l) * int(l) for l in left]))