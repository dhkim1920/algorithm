# https://www.acmicpc.net/problem/1021
from collections import deque

N, M = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
targets = list(map(int, input().split()))

result = 0
for target in targets:
    idx = queue.index(target)
    if idx <= len(queue) // 2:
        queue.rotate(-idx)
        result += idx
    else:
        move = len(queue) - idx
        queue.rotate(move)
        result += move

    queue.popleft()

print(result)






