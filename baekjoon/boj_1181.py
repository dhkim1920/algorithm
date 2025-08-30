# https://www.acmicpc.net/problem/1181

N = int(input())
words = []
for i in range(N):
    words.append(input())


def get_len(data):
    return len(data), data


sorted_arr = sorted(words, key=get_len)

print(sorted_arr[0])
for i in range(1, len(sorted_arr)):
    if sorted_arr[i] != sorted_arr[i - 1]:
        print(sorted_arr[i])
