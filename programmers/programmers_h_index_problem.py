# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    sum_citations = sum(citations)
    if sum_citations == 0:
        return 0
    elif sum_citations == 1:
        return 1
    else:
        answer = 1
        citations = sorted(citations)

        for i in range(len(citations)):
            if citations[i] == 0:
                continue
            else:


        print("--------------------")

        return answer


print(solution([3, 0, 6, 1, 5]))
# print(solution([1, 1, 5, 6]))
# print(solution([0]))
# print(solution([0, 0, 0, 1]))