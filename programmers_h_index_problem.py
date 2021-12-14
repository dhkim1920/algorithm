# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    if sum(citations) == 0:
        return answer
    else:
        print(sorted(citations))
        return answer


print(solution([3, 0, 6, 1, 5]))
# print(solution([1, 1, 5, 6]))
# print(solution([0]))
# print(solution([0, 0, 0]))