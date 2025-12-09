import sys
from functools import lru_cache

with open(sys.argv[1]) as f:
    raw_input = f.read().rstrip()

start = None
splitter_rows = tuple()

for y, line in enumerate(raw_input.split("\n")):
    splitters = frozenset()
    for x, char in enumerate(line):
        if char == "S":
            start = x
        
        if char == "^":
            splitters |= {x}
    
    if len(splitters) > 0:
        splitter_rows += (splitters,)

@lru_cache
def get_path_count(start_x: int, rows: tuple[frozenset[int]], row=0) -> int:
    if row >= len(rows):
        return 1
    
    if start_x in rows[row]:
        return get_path_count(start_x + 1, rows, row+1) + get_path_count(start_x - 1, rows, row+1)
    
    return get_path_count(start_x, rows, row+1)

print(get_path_count(start, splitter_rows))

