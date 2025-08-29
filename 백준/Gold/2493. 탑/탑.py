N = int(input())
tops = [0] + list(map(int, input().split()))
result = [0] * (N + 1)
stack = []

for i in range(1, N + 1):
    while stack:
        if tops[i] > stack[-1][0]:
            stack.pop()
        else:
            result[i] = stack[-1][1]
            break

    stack.append((tops[i], i))


print(*result[1:])