input = open("input.txt", "r")

lines = input.readlines()

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

noHands = len(lines)
handsbids = [(None,0)]* noHands

types = [[] for _ in range(7)]   # Five of a kind, Four of a kind, Full house, Three of a kind, Two pair, One pair, High card

for i, line in enumerate(lines):
    split = line.split(' ')
    handsbids[i] = (split[0], int(split[1]))
    contains = [0] * 13
    hand = handsbids[i][0]
    for j in range(len(hand)):
        contains[cards.index(handsbids[i][0][j])] += 1
    jokers = contains[-1]
    contains[-1] = 0
    
    contains.sort()
    contains.reverse()
    contains[0] += jokers
    if contains[0] == 5:
        types[0].append(handsbids[i])
    elif contains[0] == 4:
        types[1].append(handsbids[i])
    elif contains[0] == 3 and contains[1] == 2:
        types[2].append(handsbids[i])
    elif contains[0] == 3:
        types[3].append(handsbids[i])
    elif contains[0] == 2 and contains[1] == 2:
        types[4].append(handsbids[i])        
    elif contains[0] == 2:
        types[5].append(handsbids[i])
    else: 
        types[6].append(handsbids[i])
    

def sorter(hand):
    for i in range(len(hand)):
        hand[i] = cards.index(hand[i])
    return hand





ranked = [None] * noHands
rank = 0
for type in types[::-1]:
    type.sort(key=lambda x: sorter(list(x[0])))
    type = type[::-1]
    for handBid in type:
        ranked[rank] = handBid
        rank += 1

sum = 0

for i, handbid in enumerate(ranked):
    sum += handbid[1] * (i+1)

print(sum)