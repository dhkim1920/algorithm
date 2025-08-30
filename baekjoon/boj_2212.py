# https://www.acmicpc.net/problem/2212

n = int(input())
k = int(input())
arr = list(map(int, input().split()))

arr.sort()

distance = []
for i in range(0, len(arr) - 1):
    distance.append(arr[i + 1] - arr[i])

distance.sort(reverse=True)

print(sum(distance[k-1:]))
