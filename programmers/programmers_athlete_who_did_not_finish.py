# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''

    finish_dict = {k: 0 for k in participant}

    for i in participant:
        if i in finish_dict:
            finish_dict[i] += 1

    for i in completion:
        if i in finish_dict:
            finish_dict[i] -= 1

    for k in finish_dict.keys():
        if finish_dict[k] == 1:
            return k

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
