# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = []
    tmp_stack = []

    tmp = (priorities[location], location)
    # print(tmp)

    while len(priorities) > 0:
        if priorities[-1] != max(priorities):
            print("before: " + str(priorities))
            tmp_stack.append(priorities.pop())
            print("after: " + str(priorities))
            print("--------------------------")
        else:
            print("before else pop: " + str(priorities))
            v = priorities.pop()
            print("else pop: " + str(priorities))
            answer.append((v, len(priorities)))
            while len(tmp_stack) > 0:
                priorities.append((tmp_stack.pop()))
                print("else append tmp_stack: " + str(priorities))
            print("--------------------------")

    print(answer)
    return answer.index(tmp) + 1


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))