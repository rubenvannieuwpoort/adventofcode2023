INPUT_FILE = 'input.txt'

input = open(INPUT_FILE, 'r').read().splitlines()

sum = 0
for nr, line in enumerate(input):
    grabs = line.split(':')[1][1:].split('; ')

    r, g, b = 0, 0, 0
    for grab_input in grabs:
        cubes = [0, 0, 0]

        for grab in grab_input.split(', '):
            tokens = grab.split(' ')
            amount = int(tokens[0])
            color = tokens[1]
            color_nr = ['red', 'green', 'blue'].index(color)
            cubes[color_nr] = amount

        r = max(r, cubes[0])
        g = max(g, cubes[1])
        b = max(b, cubes[2])
    
    sum += r * g * b

print(sum)
