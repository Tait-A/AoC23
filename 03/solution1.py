import re

input = open("input.txt", "r")

sample_input = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....",".664.598.."]

#input = sample_input
prev_nums = []
symbols = []

sum = 0

def checkSymbol(pos, no, symbols, i):
    if i == 0:
        lines = [symbols[i], symbols[i+1]]
    elif i == len(symbols)-1:
        lines = [symbols[i-1], symbols[i]]
    else:
        lines = [symbols[i-1], symbols[i], symbols[i+1]]
    positions = list(range((pos-1),(pos+len(str(no))+1)))
    for line in lines:
        for pos in positions:
            if pos in line:
                return True
    return False
   

for line in input:

    line_symbols = []
    for i in range(len(line)):
        if not line[i].isdigit() and line[i] != ".":
            line_symbols.append(i)
    symbols.append(line_symbols[:-1])

input = open("input.txt", "r")
for i, line in enumerate(input):
    print(line, end="")
    print(symbols[i])
    summed_nos = []
    d = dict((m.start(), int(m.group())) for m in re.finditer("\d+", line))
    for (pos, no) in d.items():
        if checkSymbol(pos, no, symbols, i):
            sum += no
            summed_nos.append(no)
    print(summed_nos)
    print()


print(sum)
