# https://www.acmicpc.net/problem/2178

from collections import deque

# array_str = ["101111", "101010", "101011", "111011"]
# N = len(array_str)
# M = len(array_str[0])

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        if x == N - 1 and y == M - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= N or ny >= M:
                continue
            if maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))


print(bfs())