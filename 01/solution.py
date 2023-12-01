import re


input = open("input.txt", "r")

int_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

#input = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

sum = 0

for line in input:
    print(line, end="")
    found = []
    for i in range(9):
        if int_text[i] in line:
            finds = [m.start() for m in re.finditer(int_text[i], line)]
            for pos in finds:
                pair = (i+1, pos)
                found.append(pair)

    if found not in ([], None):
        if len(found) == 1:
            no, pos = found[0]
            line = line[:pos] + str(no) + line[pos:]
        else:
            no1, pos1 = min(list(found), key = lambda t: t[1])
            no2, pos2 = max(list(found), key = lambda t: t[1])
            line = line[:pos1] + str(no1) + line[pos1:pos2]+ str(no2) + line[pos2:]
    
    digits = ''.join(digit for digit in line if digit.isdigit())
    digits = digits[0]+digits[-1]
    number = int(digits)

    sum += number
    print(line, end="")
    print(number)
    print()

print(sum)