# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    answer = True

    phone_book = {k: 0 for k in phone_book}

    for i in phone_book.keys():
        for j in phone_book.keys():
            if i in j:
                if i is not j:
                    return False

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
print(solution(["11", "22", "111"]))
print(solution(["111", "22", "11"]))