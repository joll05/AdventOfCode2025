import sys
from math import log10

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

parsed_input = [tuple(int(number) for number in item.split("-")) for item in raw_input.split(",")]

def test_range(start, end):
    invalid_sum = 0
    for i in range(start, end+1):
        digit_string = str(i)
        digit_count = len(digit_string)
        
        id_valid = True

        for repeated_digits in range(1, digit_count):
            if digit_count % repeated_digits != 0:
                continue
            
            has_repetition = True
            check_string = digit_string[0:repeated_digits]

            for check_pos in range(repeated_digits, digit_count, repeated_digits):
                if digit_string[check_pos:check_pos+repeated_digits] != check_string:
                    has_repetition = False
                    break
            
            if has_repetition:
                id_valid = False
                break
        
        if not id_valid:
            invalid_sum += i

    return invalid_sum

print(sum(test_range(start, end) for start, end in parsed_input))