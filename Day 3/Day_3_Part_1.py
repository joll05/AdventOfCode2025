import sys
with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

banks = tuple(tuple(int(char) for char in line) for line in raw_input.split("\n"))

def find_first_largest(numbers):
    largest_number = numbers[0]
    largest_index = 0

    for i, number in enumerate(numbers):
        if number > largest_number:
            largest_number = number
            largest_index = i
    
    return (largest_number, largest_index)

def find_largest_joltage(bank):
    tens_digit, tens_index = find_first_largest(bank[:-1])
    ones_digit, _ = find_first_largest(bank[tens_index + 1:])

    return tens_digit * 10 + ones_digit

print(sum(find_largest_joltage(bank) for bank in banks))