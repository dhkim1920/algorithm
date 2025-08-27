# https://www.acmicpc.net/problem/1260

from collections import deque

# N = 4
# M = 5
# V = 1

N, M, V = map(int, input().split())

input_graph = [[] for _ in range(N + 1)]
# edges = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]

edges = []

for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

for a, b in edges:
    input_graph[a].append(b)
    input_graph[b].append(a)

for i in range(1, N + 1):
    input_graph[i].sort()


def dfs(graph, v, visited):
    stack = deque([v])

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True
            print(current, end=' ')

            for i in reversed(graph[current]):
                if not visited[i]:
                    stack.append(i)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(input_graph, V, [False] * (N + 1))
print()
bfs(input_graph, V, [False] * (N + 1))
