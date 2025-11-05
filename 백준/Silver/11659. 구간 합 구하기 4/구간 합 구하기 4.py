import sys
input = sys.stdin.readline

N, M =  map(int, input().strip().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

answers = []
for _ in range(M):
    i, j = map(int, input().split())
    s = prefix_sum[j] - prefix_sum[i - 1]
    answers.append(s)

print('\n'.join(map(str, answers)))