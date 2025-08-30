# https://www.acmicpc.net/problem/10026


# array = [
#     ['R', 'R', 'R', 'B', 'B'],
#     ['G', 'G', 'B', 'B', 'B'],
#     ['B', 'B', 'B', 'R', 'R'],
#     ['B', 'B', 'R', 'R', 'R'],
#     ['R', 'R', 'R', 'R', 'R']
# ]
#
# N = len(array)

from collections import deque

N = int(input())
array = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, c):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if nx <= -1 or ny <= -1 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny] and array[nx][ny] == c:
                queue.append((nx, ny))
                visited[nx][ny] = True


def get_result(colors):
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and array[i][j] in colors:
                bfs(i, j, array[i][j])
                result += 1
    return result


visited = [[False] * N for _ in range(N)]
normal_result = get_result(["R", "G", "B"])

for i in range(N):
    for j in range(N):
        if array[i][j] == "G":
            array[i][j] = "R"

visited = [[False] * N for _ in range(N)]
abnormal_result = get_result(["R", "B"])

print(f"{normal_result} {abnormal_result}")


"""
참고)
- recursion error 발생함
이유)
이 문제는 N이 100까지임
N X N 이므로 100 X 100 = 10000까지 수행해야 함
파이썬은 기본적으로 재귀를 약 1000회만 허용함
"""
"""
N = int(input())
array = [list(input()) for _ in range(N)]


def dfs(x, y, c):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    if visited[x][y] or array[x][y] != c:
        return False

    visited[x][y] = True
    dfs(x + 1, y, c)
    dfs(x - 1, y, c)
    dfs(x, y + 1, c)
    dfs(x, y - 1, c)
    return True


normal_result = 0
visited = [[False] * N for _ in range(N)]
for c in ["R", "G", "B"]:
    for i in range(N):
        for j in range(N):
            if dfs(i, j, c):
                normal_result += 1

for i in range(N):
    for j in range(N):
        if array[i][j] == "G":
            array[i][j] = "R"

abnormal_result = 0
visited = [[False] * N for _ in range(N)]
for c in ["R", "B"]:
    for i in range(N):
        for j in range(N):
            if dfs(i, j, c):
                abnormal_result += 1

print(f"{normal_result} {abnormal_result}")
"""
