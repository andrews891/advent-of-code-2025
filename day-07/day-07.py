import numpy as numpy

with open("input.txt", "r") as f:
    lines = [[c for c in l] for l in f.readlines()]

splits = []

for y in range(1, len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "^":
            continue

        if lines[y - 1][x] in ["S", "|"]:
            lines[y][x] = "|"

        try:
            if lines[y][x + 1] == "^" and lines[y - 1][x + 1] == "|":
                lines[y][x] = "|"
                if (x + 1, y) not in splits:
                    splits.append((x + 1, y))

            if lines[y][x - 1] == "^" and lines[y - 1][x - 1] == "|":
                lines[y][x] = "|"
                if (x - 1, y) not in splits:
                    splits.append((x - 1, y))

        except IndexError:
            continue

timeline_splits = {}

for y in range(len(lines) - 1, 0, -1):
    for x in range(len(lines[0])):
        if lines[y][x] == "^":
            left = 0
            right = 0
            for j in range(y + 1, len(lines)):
                if lines[j][x - 1] == "^":
                    if timeline_splits[(j, x - 1)]:
                        left = sum(timeline_splits[(j, x - 1)])
                        break
                if j == len(lines) - 1:
                    left = 1

            for i in range(y + 1, len(lines)):
                if lines[i][x + 1] == "^":
                    if timeline_splits[(i, x + 1)]:
                        right = sum(timeline_splits[(i, x + 1)])
                        break
                if lines[i][x + 1] != "|":
                    break
                if i == len(lines) - 1:
                    right = 1

            timeline_splits[(y, x)] = [left, right]


print(f"part 1: {len(splits)}")
print(f"part 2: {sum(list(timeline_splits.values())[-1])}")
