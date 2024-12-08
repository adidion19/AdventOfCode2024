def read_input():
    with open('input.txt', 'r') as file:
        return file.read().splitlines()

lines = read_input()

word = ['X', 'M', 'A', 'S']
tab = [list(l) for l in lines]

def continue_searching_in_the_direction(c, grid, x_step, y_step, index, row, col):

    new_row = row + x_step
    new_col = col + y_step

    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == c:
        if index + 1 == len(word):
            return 1
        return continue_searching_in_the_direction(word[index + 1], grid, x_step, y_step, index + 1, new_row, new_col)

    return 0

def search_near(grid, row, col):
    count = 0
    for x_step, y_step in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        count += continue_searching_in_the_direction(word[1], grid, x_step, y_step, 1, row, col)
    return count

def search_cross(lst, row, col):
    if not (0 <= row - 1 < len(lst) and 0 <= row + 1 < len(lst) and 0 <= col - 1 < len(lst[0]) and 0 <= col + 1 < len(lst[0])):
        return 0

    patterns = [
        (word[1], word[3], word[1], word[3]),
        (word[3], word[1], word[3], word[1]),
        (word[1], word[3], word[3], word[1]),
        (word[3], word[1], word[1], word[3])
    ]

    for p in patterns:
        if (lst[row - 1][col - 1], lst[row + 1][col + 1], lst[row + 1][col - 1], lst[row - 1][col + 1]) == p:
            return 1

    return 0


# Part 1.
counter = 0
for i in range(len(tab)):
    for j in range(len(tab[i])):
        if tab[i][j] == word[0]:
            counter += search_near(tab, i, j)

print(counter)

# Part 2.

counter = 0
for i in range(len(tab)):
    for j in range(len(tab[i])):
        if tab[i][j] == word[2]:
            counter += search_cross(tab, i, j)

print(counter)


