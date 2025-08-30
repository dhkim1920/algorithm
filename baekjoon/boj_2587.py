# https://www.acmicpc.net/problem/2587

arr = []

for i in range(5):
    arr.append(int(input()))

sorted_arr = sorted(arr)
print(int(sum(sorted_arr) / 5))
print(sorted_arr[2])
