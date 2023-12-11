INPUT_FILE = 'input.txt'

input = open(INPUT_FILE, 'r').read().splitlines()

pts = 0
for line in input:
    line_input = line.split(': ')[1].split(' | ')
    winning = [int(x) for x in line_input[0].split(' ') if x != '']
    mines = [int(x) for x in line_input[1].split(' ') if x != '']

    hits = 0
    for mine in mines:
        if mine in winning:
            hits += 1
    
    if hits:
        pts += 2 ** (hits - 1)

print(pts)
