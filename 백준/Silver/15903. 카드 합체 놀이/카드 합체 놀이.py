import heapq, sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cards)

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    s = x + y
    heapq.heappush(cards, s)
    heapq.heappush(cards, s)

print(sum(cards))