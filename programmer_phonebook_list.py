# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    answer = True

    phone_book = {k: 0 for k in phone_book}

    print(phone_book)

    for i in range(len(phone_book)):
        print(phone_book[i])

    # for i in range(len(phone_book)):
    #     for j in range(i + 1, len(phone_book)):
    #         if phone_book[i] in phone_book[j]:
    #             print(phone_book[i] + " " + phone_book[j])
    #             return False

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
