# import sys

# max = 0
# idx = 0 

# for i in range(9):
#     a = int(sys.stdin.readline())
#     if a > max:
#         max = a
#         idx = i+1

# print(max)
# print(idx)

import sys

nums = [int(sys.stdin.readline()) for i in range(9)]

result = max(nums)
print(result)
print(nums.index(result)+1)