import os

with open("input/day1-1.txt") as f:
    input_lines = f.readlines()

pos = 50
zero_count = 0
for line in input_lines:
    line = line.strip()
    dir = line[0]
    dist = int(line[1:])

    if dir == 'R':
        pos += dist
    else:
        pos -= dist

    if pos % 100 == 0:
        zero_count += 1
        print(pos)

print(zero_count)