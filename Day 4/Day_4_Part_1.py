import sys
with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

grid = tuple(tuple(char == "@" for char in line) for line in raw_input.split("\n"))

def count_adjacent(grid, x, y):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue

            test_x = x + dx
            test_y = y + dy
            if not (0 <= test_x < len(grid[0]) and 0 <= test_y < len(grid)):
                continue

            if grid[test_y][test_x]:
                count += 1
    return count

total = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if not grid[y][x]:
            continue

        count = count_adjacent(grid, x, y)
        if count < 4:
            total += 1

print(total)