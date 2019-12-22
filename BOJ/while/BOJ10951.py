# import sys
# 
# while True :
#     try:
#         a , b = map(int, sys.stdin.readline().split())
#         print(a+b)
#     except EOFError:
#         break

import sys

while True:
    for i in sys.stdin:
        a, b = map(int, i.split())
        print(a+b)