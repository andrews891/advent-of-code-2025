import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

data = np.array([[c for c in line[:-1]] for line in lines])
data = np.pad(data, ((1, 1), (1, 1)), "constant", constant_values=("."))

neighbours = np.array(
    [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
)

total = 0
for x in range(1, data.shape[0] - 1):
    for y in range(1, data.shape[1] - 1):
        rolls = 0
        if data[x, y] != "@":
            continue
        for n in neighbours:
            if rolls >= 4:
                break
            if data[[x + n[0]], [y + n[1]]] == "@":
                rolls += 1
        total += 1 if rolls < 4 else 0

print(f"part 1: {total}")
