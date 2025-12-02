with open("input.txt", "r") as file:

    total = 0
    position = 50
    wheel = 100

    for line in file:
        direction = 1 if line[0] == 'R' else -1
        rotation = int(line[1:])
        position = (position + (direction * rotation)) % wheel
        if position == 0:
            total += 1

    print(f"| Part 1 | Number of 0-rotation stops: {total}")


with open("input.txt", "r") as file:

    total = 0
    position = 50
    wheel = 100

    for line in file:
        direction = 1 if line[0] == 'R' else -1
        rotation = int(line[1:])
        for _ in range(rotation):
            position = (position + direction) % wheel
            if position == 0:
                total += 1

    print(f"| Part 2 | Number of 0-rotation passes: {total}") 
