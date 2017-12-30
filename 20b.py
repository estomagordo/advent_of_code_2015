from functools import reduce
from itertools import combinations

def solve(n):
    primes = [2, 3]
    target = n // 10
    i = int(target**0.5) + 1

    for x in range(5, i, 2):
        is_prime = True
        
        for prime in primes:
            if prime * prime > x:
                 break
            if x % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(x)
    
    while True:
        x = i
        prime_factors = []
        
        for prime in primes:
            if prime > x:
                break
            while x % prime == 0:
                x /= prime
                prime_factors.append(prime)

        factors = set([1, x])

        for number in range(1, len(prime_factors) + 1):
            for c in combinations(prime_factors, number):
                factor = reduce(lambda x, y: x * y, c)
                if 50 * factor >= i:
                    factors.add(factor)
        
        if 11 * sum(factors) >= n:            
            return i
        
        i += 1

print(solve(36000000))