from typing import List
"""
It can detect the prime in O(1) by pre computing
"""
# this algorithm take sqrt(n) TC to execute
def check_prime(n: int) -> bool:
    i: int = 2
    count: int = 0
    while i * i <= n:
        if n % i == 0:
            count += 1
        #  mitigating duplicate factors
        if n / i != i:
            count += 1
        if count > 2:
            return False
    
    return False if count > 2 else True

n: int = 2000

isPrime: List[int] = [True for i in range(n + 1)]

isPrime[0] = False
isPrime[1] = False

for i in range(2, n + 1):
    
    if isPrime[i] == False:
        continue
    # if the value is prime then mark the factors of those numbers as false
    if check_prime(isPrime[i]) == True:
        for j in range(i + i, n + 1, i):
            isPrime[j] = False

for val, ind in enumerate(isPrime):
    print(val, ind)
    