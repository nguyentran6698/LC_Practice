def solution(nums):
    s = set()

    def is_prime(num):
        if num == 0 or num == 1:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        else:
            return True

    primes = list(filter(is_prime, range(1, 1000)))
    for num in nums:
        for prime in primes:
            if num % prime == 0:
                s.add(prime)
    return len(s)


print(solution([15, 11, 11, 12, 18, 4, 5, 16]))
