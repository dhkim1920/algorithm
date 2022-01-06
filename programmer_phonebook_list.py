# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    answer = True

    phone_book_len = len(phone_book)
    for i in range(0, phone_book_len):
        for j in range(i + 1, phone_book_len):
            i_len = len(phone_book[i])
            j_len = len(phone_book[j])
            if i_len > j_len:
                if phone_book[i][:j_len] == phone_book[j]:
                    return False
            else:
                if phone_book[j][:i_len] == phone_book[i]:
                    return False

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
print(solution(["11", "22", "111"]))
print(solution(["987987", "87"]))