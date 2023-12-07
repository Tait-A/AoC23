def find_lowest(seed, seed_range, maps):
    low = seed
    high = seed + seed_range - 1
    i=0
    for m in maps:
        for line in m:
            dest, src, rng = line
            if low >= src and high < (src + rng):
                low = low + dest - src
                high = low + seed_range - 1
                break
            elif low >= src and low < (src + rng):
                seed1 = low + dest - src
                rng1 = dest + rng - seed1
                seed2 = src + rng
                rng2 = seed_range - rng1
                split1 = find_lowest(seed1, rng1, maps[i+1:])
                split2 = find_lowest(seed2, rng2, maps[i:])
                return min(split1, split2)
            elif high >= src and high < (src + rng):
                seed1 = low
                rng1 = src - low
                seed2 = dest
                rng2 = high - src
                split1 = find_lowest(seed1, rng1, maps[i:])
                split2 = find_lowest(seed2, rng2, maps[i+1:])
                return min(split1, split2)
        i += 1
    return low


file = open("input.txt", "r")
input_lines = file.readlines()

seeds = list(map(int, input_lines[0].split()[1:]))
maps = []

for line in input_lines[1:]:
    if line == "\n":
        new_array = []
        maps.append(new_array)
    elif ("map" in line):
        continue
    else:
        line = list(map(int,line.split(" ")))
        maps[-1].append(line)

indices = []

for i in range(0, len(seeds), 2):
    seed = seeds[i]
    seed_range = seeds[i + 1]
    index = find_lowest(seed, seed_range, maps)
    indices.append(index)

lowest = min(indices)
print(lowest)