# https://www.acmicpc.net/problem/2309

import sys

dwarves = [int(sys.stdin.readline()) for _ in range(9)]

end = False

a = 0
b = 0
for i in range(9):
    a = dwarves[i]
    dwarves.remove(a)
    for j in range(8):
        b = dwarves[j]
        dwarves.remove(b)
        if sum(dwarves) == 100:
            end = True
            break
        dwarves.insert(j, b)

    if end:
        break
    dwarves.insert(i, a)

dwarves.sort()
print("\n".join([str(d) for d in dwarves]))