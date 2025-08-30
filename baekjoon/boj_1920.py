# https://www.acmicpc.net/problem/1920

N = int(input())
arr_n = list(map(int, input().split()))

M = int(input())
arr_m = list(map(int, input().split()))

arr_n.sort()


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for _ in arr_m:
    print(binary_search(arr_n, _))
