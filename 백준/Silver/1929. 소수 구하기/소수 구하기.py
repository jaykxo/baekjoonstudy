import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True             # 위 조건 통과 시 소수

# -------------------- main --------------------

M, N = map(int, input().split())
primes = []

for i in range(M, N + 1):
    if is_prime(i):
        primes.append(i)

print('\n'.join(map(str, primes)))