INPUT_FILE = 'input.txt'

def preprocess(line):
    return line.replace('twone', 'twoone') \
               .replace('eightwo', 'eighttwo') \
               .replace('eighthree', 'eightthree') \
               .replace('oneight', 'oneeight') \
               .replace('sevenine', 'sevennine') \
               .replace('one', '1') \
               .replace('two', '2') \
               .replace('three', '3') \
               .replace('four', '4') \
               .replace('five', '5') \
               .replace('six', '6') \
               .replace('seven', '7') \
               .replace('eight', '8') \
               .replace('nine', '9')

input = open(INPUT_FILE, 'r').read().splitlines()

sum = 0
for line in input:
    numbers = list(filter(lambda x: '0' <= x and x <= '9', preprocess(line)))
    sum += int(numbers[0] + numbers[-1])

print(sum)
