# https://www.acmicpc.net/problem/2644
from collections import deque

n = int(input())
s, t = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)


def bfs(start, target):
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, depth + 1))
    return -1


print(bfs(s, t))
