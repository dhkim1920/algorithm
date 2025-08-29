# https://www.acmicpc.net/problem/2667


# array = [
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0]
# ]
#
#
# N = len(array)

from collections import deque

N = int(input())
array = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    count = 1
    while queue:
        cx, cy = queue.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny] and array[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count


def get_result():
    result = 0
    counts = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and array[i][j] == 1:
                count = bfs(i, j)
                result += 1
                counts.append(count)

    counts.sort()
    return result, counts


visited = [[False] * N for _ in range(N)]
result, counts = get_result()

print(result)
for count in counts:
    print(count)
