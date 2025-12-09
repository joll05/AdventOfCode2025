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
    indices = [0] + indices + [len(string)]
    for i in range(len(indices) - 1):
        output.append(string[indices[i]:indices[i+1]])
    return output

input_lines = raw_input.split("\n")
spacers = find_spacers(input_lines)

number_rows = [[int(s) for s in split_by_indices(line, spacers)] for line in input_lines[:-1]]
operator_input = [s.strip() for s in split_by_indices(input_lines[-1], spacers)]

problems = [(operator.add if op == "+" else operator.mul, [number_row[i] for number_row in number_rows]) for i, op in enumerate(operator_input)]

total = 0
for operation, numbers in problems:
    total += reduce(operation, numbers)

print(total)