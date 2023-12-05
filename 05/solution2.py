def find_lowest(seed, seed_range, maps):
    low = seed
    high = seed + seed_range - 1
    i=0
    for m in maps:
        for line in m[1:]:
            line = line.split(" ")
            dest = int(line[0])
            src = int(line[1])
            rng = int(line[2])
            print()
            print(dest, src, rng)
            print(low, high)
            if low >= src and high < (src + rng):
                low = low + dest - src
                high = low + seed_range - 1
                break
            elif low >= src and low < (src + rng):
                seed1 = low + dest - src
                rng1 = dest + rng - seed1
                seed2 = src + rng
                rng2 = seed_range - rng1
                print(seed1,rng1,seed2,rng2)
                print()
                split1 = find_lowest(seed1, rng1, maps[i+1:])
                split2 = find_lowest(seed2, rng2, maps[i:])
                return min(split1, split2)
            elif high >= src and high < (src + rng):
                seed1 = low
                rng1 = src - low
                seed2 = dest
                rng2 = high - src
                print(seed1,rng1,seed2,rng2)
                print()
                split1 = find_lowest(seed1, rng1, maps[i:])
                split2 = find_lowest(seed2, rng2, maps[i+1:])
                return min(split1, split2)
        i += 1
    return low


file = open("input.txt", "r")
input_lines = file.readlines()

seeds = list(map(int, input_lines[0].split()[1:]))
maps = []
rest = input_lines[1:]


for line in rest:
    if line == "\n":
        new_array = []
        maps.append(new_array)
    else:
        maps[-1].append(line)

indices = []

for i in range(0, len(seeds), 2):
    seed = seeds[i]
    seed_range = seeds[i + 1]
    index = find_lowest(seed, seed_range, maps)
    indices.append(index)

lowest = indices[0]

for i in range(len(indices)):
    if indices[i] < lowest:
        print(lowest)
        lowest = indices[i]
        lowest_seed = seeds[i]

print(lowest)