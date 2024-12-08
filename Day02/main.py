def read_input():
    with open('input.txt', 'r') as file:
        return file.read().splitlines()

lines = read_input()

def count_near_values(lst):
    return all((0 < int(lst[i + 1]) - int(lst[i]) < 4) for i in range(len(lst) - 1))

# Part 1.
print(sum([count_near_values(l.split()) or count_near_values(l.split()[::-1]) for l in lines]))

# Part 2.
counter = 0
for l in lines:
    l = l.split()
    if count_near_values(l) or count_near_values(l[::-1]):
        counter += 1
        continue
    for j in range(len(l)):
        if count_near_values(l[:j]+l[j+1:]) or count_near_values((l[:j]+l[j+1:])[::-1]):
            counter += 1
            break

print(counter)
