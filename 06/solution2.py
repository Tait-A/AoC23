input = open("input.txt", "r")

lines = input.readlines()


times = lines[0]
distances = lines[1]

time = int(''.join(times.split()[1:]))
distance = int(''.join(distances.split()[1:]))

noWays = 0

dists = [0] * (time+1)
for j in range(time+1):
    dists[j] = j * (time-j)
    if dists[j] > distance:
        noWays += 1


print(noWays)
    
