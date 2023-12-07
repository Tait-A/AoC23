import numpy as np

input = open("input.txt", "r")

lines = input.readlines()


times = lines[0]
distances = lines[1]

times = list(map(int, times.split()[1:]))
distances = list(map(int, distances.split()[1:]))

noRaces = len(times)
noWays = [0] * noRaces

for i in range(noRaces):
    dists = [0] * (times[i]+1)
    for j in range(times[i]+1):
        dists[j] = j * (times[i]-j)
        if dists[j] > distances[i]:
            noWays[i] += 1

product = np.prod(noWays)

print(product)
    
