import sys
with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

start = None
splitter_rows = []

for y, line in enumerate(raw_input.split("\n")):
    splitters = []
    for x, char in enumerate(line):
        if char == "S":
            start = x
        
        if char == "^":
            splitters.append(x)
    
    if len(splitters) > 0:
        splitter_rows.append(splitters)

beams = {start}
splits = 0


for row in splitter_rows:
    for splitter in row:
        if splitter in beams:
            splits += 1
            beams.remove(splitter)
            beams.add(splitter + 1)
            beams.add(splitter - 1)

print(splits)

