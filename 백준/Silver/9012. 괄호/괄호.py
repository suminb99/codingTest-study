def checkVPS(ps):
    stack = []

    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

numInput = int(input())
inputList = [input() for i in range(numInput)]

for i in inputList:
    valid = checkVPS(i)
    if valid: print("YES")
    else: print("NO")
