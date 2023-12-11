INPUT_FILE = 'input.txt'

input = open(INPUT_FILE, 'r').read().splitlines()

sum = 0
for line in input:
    numbers = list(filter(lambda x: '0' <= x and x <= '9', line))
    sum += int(numbers[0] + numbers[-1])

print(sum)
