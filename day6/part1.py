from math import floor, sqrt

INPUT_FILE = 'input.txt'

input = open(INPUT_FILE, 'r').read().splitlines()
times = list(map(lambda x: int(x), filter(lambda x: x != '', input[0].split(':')[1].strip().split(' '))))
records = list(map(lambda x: int(x), filter(lambda x: x != '', input[1].split(':')[1].strip().split(' '))))

prod = 1
for i in range(0, len(times)):
    time = times[i]
    record = records[i]
    s = floor((time - sqrt(time * time - 4 * record)) / 2) + 1
    prod *= 1 + time - 2 * s

print(prod)
