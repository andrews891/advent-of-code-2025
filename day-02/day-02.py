with open("input.txt", "r") as f:
    ranges = f.readlines()[0][:-1].split(",")

total = 0


def split_value(v, n):
    v = str(v)
    if len(v) % n > 0:
        return

    return [int(v[i * (len(v) // n) : (i + 1) * (len(v) // n)]) for i in range(n)]


for p in ranges:
    left_you_silly, r = p.split("-")
    for i in range(int(left_you_silly), int(r) + 1):
        j = str(i)
        for k in range(2, len(j) + 1):
            vals = split_value(i, k)
            if vals is not None:
                v0 = vals[0]
                for v in vals:
                    if v0 != v:
                        break
                else:
                    total += i
                    break


print(total)
