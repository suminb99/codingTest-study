import sys

n = int(input())
seq = list(map(int, input().split()))
p = -1

# 끝에서부터 순회했을 때 내림차순이 끝나는 지점 찾기
for i in range(n-1, 0, -1):
    if seq[i-1] > seq[i]:
        p = i-1
        break

# 순열이 오름차순일 때
if (p == -1 or n == 1):
    print(-1)
    sys.exit()

for i in range(n-1, 0, -1) :
    if seq[i] < seq[p]:
        seq[i], seq[p] = seq[p], seq[i]
        break

seq = seq[:p+1] + sorted(seq[p+1:], reverse=True)
print(*seq)

