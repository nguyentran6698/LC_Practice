def solution(n):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n = n // i
                factors.append(i)
        # you still have number
        if n > 1:
            factors.append(n)
        
        return factors 

    num = n
    seen = set()
    while True:
        factors = prime_factors(n)
        if len(factors) == 1:
            return factors[0]
        num = sum(factors)
        if num in seen:
            break
        seen.add(num)
    return num


