import sys
from math import ceil

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

input_lines = raw_input.split("\n")

instructions = [(line[0], int(line[1:])) for line in input_lines]

current_position = 50
zero_count = 0

for direction, amount in instructions:
    direction_int = (1 if direction == "R" else -1)
    
    while amount > 0:
        current_position += direction_int
        current_position %= 100
        if current_position == 0:
            zero_count += 1
        amount -= 1

print(f"Zero count: {zero_count}")