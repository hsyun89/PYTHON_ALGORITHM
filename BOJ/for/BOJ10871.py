import sys

n, lim = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(n):
    if num_list[i] < lim:
        result.append(num_list[i])

for i in range(len(result)):
    print(result[i], end=" ")