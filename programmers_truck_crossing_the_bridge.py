# https://programmers.co.kr/learn/courses/30/lessons/42587


def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_crossing_bridge = []
    bridge = []

    while truck_weights:
        if weight < sum(bridge):
            bridge.append(truck_weights.pop())

    

        answer = answer + 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
