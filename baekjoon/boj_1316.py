# https://www.acmicpc.net/problem/1316

N = int(input())
words = []
for i in range(N):
    words.append(input())


def solution():
    result = 0
    for word in words:
        l = len(word)
        if l <= 1:
            result += 1
            continue

        seen = [word[0]]
        is_group_word = True
        for c in range(1, l):
            if word[c - 1] != word[c]:
                if word[c] not in seen:
                    seen.append(word[c])
                else:
                    is_group_word = False
                    break

        if is_group_word:
            result += 1

    return result


print(solution())
