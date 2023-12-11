INPUT_FILE = 'input.txt'

def parse_map(input):
    actual_input = input.split(':\n')[1].splitlines()
    return [parse_map_section(*[int(y) for y in x.split(' ')]) for x in actual_input]

def parse_map_section(dest_start, source_start, length):
    return (source_start, source_start + length, dest_start - source_start)

def lookup(value, map):
    for (start, end, offset) in map:
        if start <= value and value < end:
            return value + offset
    return value

def f(x, maps):
    for map in maps:
        x = lookup(x, map)
    return x

input = open(INPUT_FILE, 'r').read().split('\n\n')

seeds = [int(x) for x in input[0].split('seeds: ')[1].split(' ')]
maps = list(parse_map(x) for x in input[1:])

print(min(f(s, maps) for s in seeds))
