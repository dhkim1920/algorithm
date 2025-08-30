# https://www.acmicpc.net/problem/2606

# CN = 7
# E = 6
# target_graph = [
#     [1, 2],
#     [2, 3],
#     [1, 5],
#     [5, 2],
#     [5, 6],
#     [4, 7]
# ]

CN = int(input())
E = int(input())
target_graph = [map(int, input().split()) for _ in range(E)]


def dfs(graph, v, visited):
    visited[v] = True
    if v > 1:
        result = 1
    else:
        result = 0

    for i in graph[v]:
        if not visited[i]:
            result += dfs(graph, i, visited)

    return result


graph = [[] for _ in range(CN + 1)]
visited = [False] * (CN + 1)

for a, b in target_graph:
    graph[a].append(b)
    graph[b].append(a)

print(graph)

print(dfs(graph, 1, visited))


# def dfs(graph, v, visited):
#     stack = [v]
#     visited[v] = True
#     count = 0
#
#     while stack:
#         current = stack.pop()
#         for neighbor in graph[current]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 stack.append(neighbor)
#                 count += 1
#
#     return count
