# Link: https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []

    for command in commands:
        tmp_array = array[command[0] - 1:command[1]]
        for i in range(len(tmp_array) - 1, 0, -1):
            for j in range(i):
                if tmp_array[j] > tmp_array[j + 1]:
                    tmp_array[j], tmp_array[j + 1] = tmp_array[j + 1], tmp_array[j]
        answer.append(tmp_array[command[2] - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
