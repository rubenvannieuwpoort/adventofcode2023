INPUT_FILE = 'input.txt'

input = open(INPUT_FILE, 'r').read().splitlines()

instructions = input[0]
graph = {}
for line in input[2:]:
    parts = line.split(' = ')
    dirs = parts[1][1:-1].split(', ')
    graph[parts[0]] = dirs

cur = 'AAA'
i = 0
while cur != 'ZZZ':
    cur = graph[cur]['LR'.index(instructions[i % len(instructions)])]
    i += 1

print(i)
