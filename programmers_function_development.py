# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []

    progresses = list(reversed(progresses))
    speeds = list(reversed(speeds))

    while True:
        if len(progresses) == 0:
            break

        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        progresses_len = len(progresses)
        while True:
            try:
                if progresses[-1] >= 100:
                    progresses.pop()
                else:
                    break
            except IndexError as e:
                break

        if progresses_len - len(progresses) > 0:
            answer.append(progresses_len - len(progresses))

    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([0, 1], [99, 99]))