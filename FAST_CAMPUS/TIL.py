#배열
# dataset = ['mical','Mical','MMMical']

# m_count = 0
# for data in dataset:
#     for idx in range(len(data)):
#         if data[idx] == 'M':
#             m_count += 1

# print(m_count)

#큐
import queue
data_queue = queue.Queue()

data_queue.put("funcocding")
data_queue.put(1)

print(data_queue.qsize()) 

#우선순위 큐
import queue

data_queue = queue.PriorityQueue()

data_queue.put((10, "korea"))
data_queue.put((5,1))
data_queue.put((15,"china"))

data_queue.qsize()
print(data_queue.get())

#리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))
print(dequeue())
print(dequeue())