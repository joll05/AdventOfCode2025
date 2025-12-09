import operator
import sys
from functools import reduce

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

range_input, ingredient_input = raw_input.split("\n\n")

ranges = tuple()

for line in range_input.split("\n"):
    start, end = map(int, line.split("-"))
    ranges += (range(start, end+1),)

# ingredients = tuple(int(line) for line in ingredient_input.split("\n"))

def ranges_overlap(range_a: range, range_b: range):
    return range_a.start < range_b.stop and range_b.start < range_a.stop

def consolidate_ranges(range_a: range, range_b: range):
    return range(min(range_a.start, range_b.start), max(range_a.stop, range_b.stop))

def consolidate_all_ranges(ranges):
    result = []
    remaining_ranges = list(ranges)

    while len(remaining_ranges) > 0:
        range_to_consolidate = remaining_ranges.pop()
        can_consolidate_further = True

        while can_consolidate_further:
            can_consolidate_further = False

            new_remaining_ranges = []

            for range_b in remaining_ranges:
                if ranges_overlap(range_to_consolidate, range_b):
                    can_consolidate_further = True
                    range_to_consolidate = consolidate_ranges(range_to_consolidate, range_b)
                else:
                    new_remaining_ranges.append(range_b)
            
            remaining_ranges = new_remaining_ranges
        
        result.append(range_to_consolidate)
    
    return result

print(sum(len(r) for r in consolidate_all_ranges(ranges)))