"""
#스택
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)

recursive(4)

#결과
4
3
2
1
0
ended
returned 0
returned 1
returned 2
returned 3
returned 4


data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())
print(data_stack)

"""

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(stack_list)
print(pop())
