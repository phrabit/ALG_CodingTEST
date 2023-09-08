from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
result = []

deq = deque([i for i in range(1, n+1)])

while True:
    if len(deq) == 1:
        result.append(deq[0])
        break;

    result.append(deq.popleft())
    #print(result)
    deq.append(deq.popleft())

for i in result:
    print(i, end=" ")