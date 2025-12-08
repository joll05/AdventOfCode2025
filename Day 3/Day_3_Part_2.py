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

ACTIVE_BATTERIES = 12

def find_largest_joltage(bank):
    joltage = 0
    start = 0

    for digit in range(ACTIVE_BATTERIES - 1, -1, -1):
        number, index = find_first_largest(bank[start:len(bank) - digit])
        joltage += number * 10 ** digit
        start += index + 1
    
    return joltage

print(sum(find_largest_joltage(bank) for bank in banks))