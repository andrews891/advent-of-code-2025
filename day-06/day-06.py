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
results = np.tile(0, operations.shape)
numbers = np.array([list(line.replace("\n", "")) for line in lines[:-1]]).T
numbers = np.array(
    [r.replace(" ", "") for r in ["".join(row) for row in numbers.tolist()]]
)
numbers = numbers[np.where(numbers != "")]
print(numbers)
p_size = numbers.shape[0] // operations.shape[0]
numbers = np.reshape(numbers, (-1, p_size))
numbers = np.array(numbers, dtype=np.int64)

for i, operation in enumerate(operations):
    if operation == "+":
        results[i] = np.sum(numbers[i])
    else:
        results[i] = np.prod(numbers[i])

print(f"part 2: {np.sum(results)}")
