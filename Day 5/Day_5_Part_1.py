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

ingredients = tuple(int(line) for line in ingredient_input.split("\n"))

def count_fresh_ingredients(ranges, ingredients):
    return reduce(operator.add, (int(any(ingredient in a_range for a_range in ranges)) for ingredient in ingredients))

print(count_fresh_ingredients(ranges, ingredients))