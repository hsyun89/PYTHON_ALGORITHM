import sys

origin = int(sys.stdin.readline())
result = origin
count=0

while True:
    if result<10:
        result = result*10 + result
    else:
        result = (result%10)*10 + (result//10 + result%10)%10
    count += 1
    if origin == result:
        break

print(count)