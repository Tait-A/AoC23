import re

input = open("input.txt", "r")

sample_input = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....",".664.598.."]

input = input.read().split("\n")
prev_nums = []
symbols = []

sum = 0

def twoNums(star, i):
    print(i, star)
    if i == 0:
        lines = [input[i], input[i+1]]
    elif i == len(symbols)-1:
        lines = [input[i-1], input[i]]
    else:
        lines = [input[i-1], input[i], input[i+1]]
    nums = [dict((m.start(), int(m.group())) for m in re.finditer("\d+", line)) for line in lines]

    numbersIwant = []
    for num in nums:
        for (pos, no) in num.items():
            if star in list(range((pos-1),(pos+len(str(no))+1))):
                numbersIwant.append(no)

    print(numbersIwant)
    if len(numbersIwant) == 2:
        return numbersIwant[0] * numbersIwant[1]
    return 0

            

   

for line in input:
    line_symbols = []
    for i in range(len(line)):
        if line[i] in "*":
            line_symbols.append(i)
    symbols.append(line_symbols)



for i, line in enumerate(symbols):
    for star in line:
        sum += twoNums(star, i)


print(sum)
