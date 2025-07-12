import sys
from collections import deque

def operation(inputs, deque):
    inputList = inputs.split()
    command = inputList[0]

    if (not deque and command in ["pop", "front", "back"]):
        print(-1)
        return
    
    if (command == "push"):
        x = int(inputList[-1])
        deque.append(x)

    elif (command == "pop"):
        removed = deque.popleft()
        print(removed)
        
    elif command == "size":
        print(len(deque))

    elif command == "empty":
        if deque: print(0)
        else: print(1)

    elif command == "front":
        print(deque[0])

    elif command == "back":
        print(deque[-1])


d = deque([])
num = int(sys.stdin.readline())
for _ in range(num):
    inputs = sys.stdin.readline()
    operation(inputs, d)