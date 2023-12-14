from collections import defaultdict


def get_type(strengths):
    freqs = sorted(get_frequencies(strengths))
    if freqs == [1, 1, 1, 1, 1]:
        return 0
    if freqs == [1, 1, 1, 2]:
        return 1
    if freqs == [1, 2, 2]:
        return 2
    if freqs == [1, 1, 3]:
        return 3
    if freqs == [2, 3]:
        return 4
    if freqs == [1, 4]:
        return 5
    if freqs == [5]:
        return 6
    assert False


def get_frequencies(cards):
    d = defaultdict(lambda: 0)
    for card in cards:
        d[card] += 1
    return sorted(d.values())


INPUT_FILE = 'input.txt'

input = open(INPUT_FILE, 'r').read().splitlines()

hands = []
for line in input:
    things = line.split(' ')
    cards = ["23456789TJQKA".index(card) for card in things[0]]
    type = get_type(cards)
    bid = int(things[1])
    hands.append(((type, cards), bid))

hands.sort(key=lambda h: h[0])

print(sum([(i + 1) * hands[i][1] for i in range(0, len(hands))]))
