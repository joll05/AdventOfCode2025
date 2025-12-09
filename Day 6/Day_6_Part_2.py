import sys
import operator
from functools import reduce

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

def find_spacers(lines):
    length = min(len(line) for line in lines)
    spacers = []

    for i in range(length):
        if all(line[i] == " " for line in lines):
            spacers.append(i)
    
    return spacers

def split_by_indices(string, indices) -> list[str]:
    output = []
    indices = [-1] + indices + [len(string)]
    for i in range(len(indices) - 1):
        output.append(string[indices[i]+1:indices[i+1]])
    return output

input_lines = raw_input.split("\n")
spacers = find_spacers(input_lines)

number_rows = [split_by_indices(line, spacers) for line in input_lines[:-1]]

number_input = []

for column in range(len(number_rows[0])):
    numbers = []
    for char_index in range(len(number_rows[0][column])):
        number = "".join(row[column][char_index] for row in number_rows)
        numbers.append(int(number))
    number_input.append(numbers)

operator_input = [(operator.add if s.strip() == "+" else operator.mul) for s in split_by_indices(input_lines[-1], spacers)]

problems = zip(operator_input, number_input)

total = 0
for operation, numbers in problems:
    total += reduce(operation, numbers)

print(total)