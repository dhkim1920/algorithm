# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(bridge_length, weight, truck_weights):
    global first
    answer = 0

    truck_weights = deque(list(map(lambda x: [x, 0], truck_weights)))
    truck_crossing_bridge = deque()
    bridge = deque()

    print("truck_weights: " + str(truck_weights))
    print("sum: " + str(list(map(sum, truck_weights))))

    start_len = len(truck_weights)

    while len(truck_crossing_bridge) < start_len:
        if truck_weights:
            first = truck_weights[0][0]

        if len(truck_weights) > 0 & (weight > sum(list(map(sum, bridge))) + first):
            bridge.append(truck_weights.popleft())
            # tmp = truck_weights.popleft()
            # bridge.append([tmp[0], tmp[1] + 1])

        for i in range(len(bridge)):
            bridge[i][1] = bridge[i][1] + 1
            print("test: " + str(bridge))
            if bridge[i][1] == bridge_length:
                truck_crossing_bridge.append(bridge.popleft())

        print("arrive: " + str(truck_crossing_bridge))
        answer = answer + 1

    return answer


# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
