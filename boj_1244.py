# https://www.acmicpc.net/problem/1244

# switch_cnt = 8
# switches = [-1, 0, 1, 0, 1, 0, 0, 0, 1]
#
# people = 2
# boy, boy_switch = 1, 3
# girl, girl_switch = 2, 3
# people_with_pos = [(boy, boy_switch), (girl, girl_switch)]

import sys

switch_cnt = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
switches.insert(0, -1)

people = int(sys.stdin.readline())
people_with_pos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(people)]


def solution():
    for person, pos in people_with_pos:
        if person == 1:
            for k in range(pos, switch_cnt + 1, pos):
                switches[k] ^= 1
        else:
            l, r = pos - 1, pos + 1
            while l >= 1 and r <= switch_cnt and switches[l] == switches[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            for k in range(l, r + 1):
                switches[k] ^= 1

solution()
for i in range(1, switch_cnt + 1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()
if switch_cnt % 20 != 0:
    print()
