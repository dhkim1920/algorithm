# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = []
    tmp_stack = []

    priorities = [[x, i] for i, x in enumerate(priorities)]
    print(priorities)
    tmp = (priorities[location])
    print(tmp)

    while len(priorities) > 0:
        m = max(priorities)
        if priorities[-1] != m:
            tmp_stack.append(priorities.pop())
            print("after not max pop: " + str(priorities))
            print("--------------------------")
        else:
            v = priorities.pop()
            print("else max pop: " + str(priorities))
            answer.append(v)
            if len(priorities) > 0:
                t = priorities[-1] == max(priorities)
            while len(tmp_stack) > 0:
                # print("while : " + str(priorities) + " , top: " + str(priorities[-1]) + ", max: " + str(m))
                if t:
                    answer.append(tmp_stack.pop())
                    print("else append tmp_stack to answer: " + str(answer))
                else:
                    priorities.append(tmp_stack.pop())
                    print("else append tmp_stack to priorities: " + str(priorities))
            print("--------------------------")

    print(answer)
    return answer.index(tmp) + 1



# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))