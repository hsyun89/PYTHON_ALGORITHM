import sys

nums = list(map(int, sys.stdin.readline().split(" ")))
flag = 0

if nums[0] == 1:
    for i in range(8):
        if nums[i] != i+1:
            flag = 1
    if flag == 1:
        print("mixed")
    else:
        print("ascending")
elif nums[0] ==8:
    for i in range(8):
        if nums[i] != 8-i:
            flag = 1
    if flag == 1:
        print("mixed")
    else:
        print("descending")
else:
    print("mixed")

