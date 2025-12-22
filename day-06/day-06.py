import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

numbers = np.array(
    [line.replace("\n", "").split() for line in lines[:-1]], dtype=np.int64
).T
operations = np.array(lines[-1].replace("\n", "").split())
results = np.tile(0, operations.shape)

for i, operation in enumerate(operations):
    if operation == "+":
        results[i] = np.sum(numbers[i])
    else:
        results[i] = np.prod(numbers[i])

print(f"part 1: {np.sum(results)}")

results = []

numbers = np.array([[char for char in line.replace("\n", "")] for line in lines])

register = []

for c in range(numbers.shape[1] - 1, -1, -1):
    num = "".join(numbers[:, c])
    num, op = num[:-1].strip(), num[-1]

    if num == "":
        register = []
        continue

    register.append(num)

    if op == "+":
        results.append(np.sum(np.array(register, dtype=np.int64)))
    elif op == "*":
        results.append(np.prod(np.array(register, dtype=np.int64)))


print(f"part 2: {np.sum(np.array(results, dtype=np.int64))}")
