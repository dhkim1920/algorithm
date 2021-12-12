# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    longest_len = len(str(max(numbers)))

    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            a = numbers[j] if len(str(numbers[j])) >= longest_len else numbers[j] * 10
            b = numbers[j + 1] if len(str(numbers[j + 1])) >= longest_len else numbers[j + 1] * 10

            if a < b:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            elif a == b:
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


    return ''.join(map(str, numbers))


# print(solution([0, 0, 0]))
# print(solution([3, 30, 34, 5, 9]))
print(solution([3030, 303]))
