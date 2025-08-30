# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = []

    values = {x: priorities[x] for x in range(0, len(priorities))}
    indices = deque([i for i in range(0, len(priorities))])

    while indices:
        if values[indices[0]] < max(priorities):
            indices.append(indices.popleft())
        else:
            answer.append(indices[0])
            priorities.remove(values[indices.popleft()])
    return answer.index(location) + 1


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
