import sys
#specific한 경우
# result=1
# for i in range(3):
#     result *= int(sys.stdin.readline())

# 제너럴한입력
nums = [int(sys.stdin.readline()) for i in range(3)]

result = 1

for i in range(len(nums)):
    result = result * nums[i]
    
###
result = str(result)

for i in range(10):
    print(result.count(str(i)))