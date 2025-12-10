import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

data = np.array([[c for c in line[:-1]] for line in lines])
data = np.pad(data, ((1, 1), (1, 1)), "constant", constant_values=("."))

neighbours = np.array(
    [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
)

roll_mask = np.tile(False, data.shape)

changed = True
part_1 = True
part_1_total = 0
total = 0

while changed:
    changed = False
    data[roll_mask] = "."
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
            if rolls < 4:
                total += 1
                roll_mask[x, y] = True
                changed = True
    if part_1:
        part_1_total = total
        part_1 = False

print(f"part 1: {part_1_total}")
print(f"part 2: {total}")
