# https://www.acmicpc.net/problem/14503

import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

result = 1
arr[r][c] = -1

while True:
    moved = False

    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if arr[nx][ny] == 0:
            r, c = nx, ny
            arr[r][c] = -1
            result += 1
            moved = True
            break

    if moved:
        continue

    back = (d + 2) % 4
    br, bc = r + dx[back], c + dy[back]
    if arr[br][bc] == 1:
        break
    r, c = br, bc

print(result)


