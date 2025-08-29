# https://www.acmicpc.net/problem/2751
# 이건 얼핏봐서 정렬문제 같지만 파이썬 사용시 input으로 입력을 받으면 시간초과가 난다.
# 따라서 input() 을 쓰지말고 sys.stdin.readline()을 쓰면 해결된다.
# 단순 정렬문젠데 실버5인 이유는 sys.stdin.readline()를 떠올리지 못하는 경우가 있어서 인거 같다
# 참고로 python sort는 Tim sort로 merge + insertion sort 결합된 정렬 알고리즘이다
# 보통 nlogn의 복잡도를 갖고 정렬이 잘되있으면 n까지도 되니 참고

import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
sys.stdout.write('\n'.join(map(str, arr)))


