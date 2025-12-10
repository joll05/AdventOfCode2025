import sys
with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

tiles = [tuple(map(int, line.split(","))) for line in raw_input.split("\n")]

max_area = 0

for i, (x1, y1) in enumerate(tiles):
    for x2, y2 in tiles[i+1:]:
        area = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
        if area > max_area:
            max_area = area

print(max_area)