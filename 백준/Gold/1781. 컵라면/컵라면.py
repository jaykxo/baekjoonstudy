import heapq
import sys

input = sys.stdin.readline

N = int(input())
problems = []

for _ in range(N):
    date, ramen = map(int, input().split())
    problems.append((date, ramen))

problems.sort(key=lambda x: x[0])

heap = []

for date, ramen in problems:
    heapq.heappush(heap, ramen)

    if len(heap) > date:
        heapq.heappop(heap)

print(sum(heap))