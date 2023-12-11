INPUT_FILE = 'input.txt'

def is_close(symbol, part):
    (sx, sy) = symbol
    ((px0, px1), py, part_num) = part
    horizontally_close = px0 - 1 <= sx and sx <= px1 + 1
    vertically_close = abs(sy - py) <= 1
    return horizontally_close and vertically_close

input = open(INPUT_FILE, 'r').read().splitlines()

parts = []
symbols = []
current_part = 0
startpos = 0
for y, line in enumerate(input):
    for pos, c in enumerate(line):
        if c.isnumeric():
            if not current_part:
                startpos = pos
            current_part = current_part * 10 + int(c)
        else:
            if c != '.':
                symbols.append((pos, y))
            if current_part:
                parts.append(((startpos, pos - 1), y, current_part))
                current_part = 0
    if current_part:
        parts.append(((startpos, pos), y, current_part))
        current_part = 0

sum = 0
for part in parts:
    part_num = part[2]
    if any(is_close(symbol, part) for symbol in symbols):
        sum += part_num

print(sum)
