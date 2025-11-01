import sys

n = int(sys.stdin.readline())

for _ in range(n):

    left = []
    right = []

    pwd = list(sys.stdin.readline().rstrip())

    for ch in pwd:

        if ch == ">":
            if right:
                left.append(right.pop()) 

        elif ch == "<":
            if left:
                right.append(left.pop())

        elif ch == "-":
            if left:
                left.pop()

        else:
            left.append(ch)

    print(''.join(left + list(reversed(right))))