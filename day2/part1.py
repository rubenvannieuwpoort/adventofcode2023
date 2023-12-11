INPUT_FILE = 'input.txt'

red_cubes = 12
green_cubes = 13
blue_cubes = 14

input = open(INPUT_FILE, 'r').read().splitlines()

sum = 0
for nr, line in enumerate(input):
    grabs = line.split(':')[1][1:].split('; ')
    
    possible = True
    for grab_input in grabs:
        cubes = [0, 0, 0]

        for grab in grab_input.split(', '):
            tokens = grab.split(' ')
            amount = int(tokens[0])
            color = tokens[1]
            color_nr = ['red', 'green', 'blue'].index(color)
            cubes[color_nr] = amount

        if cubes[0] > red_cubes or cubes[1] > green_cubes or cubes[2] > blue_cubes:
            possible = False
            break

    if possible:
        sum += nr + 1

print(sum)
