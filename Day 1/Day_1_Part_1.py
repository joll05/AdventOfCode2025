import sys
with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

input_lines = raw_input.split("\n")

instructions = [(line[0], int(line[1:])) for line in input_lines]

current_position = 50
zero_count = 0

for direction, amount in instructions:
    match direction:
        case "R":
            current_position += amount
        case "L":
            current_position -= amount
    
    current_position %= 100

    if current_position == 0:
        zero_count += 1

print(f"Zero count: {zero_count}")