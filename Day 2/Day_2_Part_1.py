import sys
from math import log10

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

parsed_input = [tuple(int(number) for number in item.split("-")) for item in raw_input.split(",")]

def test_range(start, end):
    invalid_sum = 0
    for i in range(start, end+1):
        digit_count = int(log10(i))
        
        if digit_count % 2 != 0:
            continue
        
        power = 10 ** ((digit_count) // 2)
        prefix = i // power
        suffix = i % power

        if prefix == suffix:
            invalid_sum += i
    
    return invalid_sum

print(sum(test_range(start, end) for start, end in parsed_input))