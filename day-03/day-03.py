import numpy as np


def part1():
    total = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = [[int(c) for c in line[:-1]] for line in lines]

    data = np.array(lines)

    a = np.argmax(data[:, :-1], axis=1)
    mask = (
        np.reshape(
            np.tile(np.arange(data.shape[1]), data.shape[0]),
            data.shape,
        ).T
        > a
    ).T
    b = np.argmax(data * np.array(mask, dtype=np.int64), axis=1)

    c = data[np.arange(data.shape[0]), a]
    d = data[np.arange(data.shape[0]), b]

    total = np.sum((10 * c) + d)
    print(f"Part 1: {total}")


def part2():
    total = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = [[int(c) for c in line[:-1]] for line in lines]

    data = np.array(lines)

    for i in range(12):
        print(i)
        a = np.argmax(data[:, : -(11 - i) if i <= 10 else None], axis=1)
        total = (total * 10) + data[np.arange(data.shape[0]), a]
        mask = (
            np.reshape(
                np.tile(np.arange(data.shape[1]), data.shape[0]),
                data.shape,
            ).T
            > a
        ).T
        data *= mask

    print(f"Part 2: {np.sum(total)}")


if __name__ == "__main__":
    part1()
    part2()
