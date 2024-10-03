import sys

input = sys.stdin.readline
n = int(input())

# 소수를 구하는 에라토스테네스의 체 함수
def get_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]

primes = get_primes(n)

# 투 포인터를 사용하여 연속된 소수의 합으로 N을 만드는 경우의 수 구하기
count = 0
left, right = 0, 0
current_sum = 0

# 투 포인터를 이용해 연속된 소수의 합을 구함
while True:
    if current_sum >= n:
        current_sum -= primes[left]
        left += 1
    elif right == len(primes):
        break
    else:
        current_sum += primes[right]
        right += 1

    if current_sum == n:
        count += 1

print(count)