from collections import deque

target_graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

"""
특징
- 코드 간결 직관적
- 깊이 제한 이슈 RecursionError 발생 야기 (대략 1000번 정도)
- 재귀 호출 스택에 의해 스택 오버플로우 가능성
"""
dfs(target_graph, 1, [False] * 9)
print()


def dfs_stack(graph, v, visited):
    stack = deque([v])
    visited[v] = True
    print(v, end=' ')

    while stack:
        current = stack[-1]
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                print(i, end=' ')
                break
        else:
            stack.pop()


dfs_stack(target_graph, 1, [False] * 9)
print()


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


bfs(target_graph, 1, [False] * 9)
