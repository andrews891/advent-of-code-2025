import numpy as np
from operator import itemgetter

with open("input.txt", "r") as f:
    fresh, avail = f.read().split("\n\n")
    fresh, avail = fresh.split("\n"), [a for a in avail.split("\n") if a != ""]

fresh = np.array([f.split("-") for f in fresh], dtype=np.int64)
avail = np.array(avail, dtype=np.int64)

total = 0
for a in avail:
    for f in fresh:
        if f[0] <= a and f[1] >= a:
            total += 1
            break

print(f"part 1: {total}")


total = 0
fresh_labeled = [(int(f0), i + 1) for i, f0 in enumerate(fresh[:, 0])] + [
    (int(f1), -(i + 1)) for i, f1 in enumerate(fresh[:, 1])
]
fresh_labeled = sorted(fresh_labeled, key=itemgetter(0))
stack = []
total = 0
lo = np.inf

for item in fresh_labeled:
    if item[1] > 0:
        stack.append(item[1])
        lo = min(lo, item[0])
    else:
        del stack[stack.index(-item[1])]

    if len(stack) == 0:
        total += item[0] + 1 - lo
        lo = np.inf

print(f"part 2: {total}")
