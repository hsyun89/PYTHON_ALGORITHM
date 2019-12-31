import sys

max = 0
idx = 0 

for i in range(9):
    a = int(sys.stdin.readline())
    if a > max:
        max = a
        idx = i+1

print(max)
print(idx)