# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers_str = sorted(list(map(lambda x: str(x) * 3, numbers)), reverse=True)
    result = list(map(lambda x: x[:len(x)//3], numbers_str))

    return str(int(''.join(result)))


# print(solution([0, 0, 0]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([3030, 303]))
print(solution([998, 9]))