class Solution:
    def countNumbers(self, n):
        # code here
        def sieve(limit):
            isPrime = [True] * (limit + 1)
            isPrime[0] = isPrime[1] = False
            for i in range(2, int(math.sqrt(limit)) + 1):
                if isPrime[i]:
                    for j in range (i*i, limit + 1, i):
                        isPrime[j] = False
            return [i for i, val in enumerate(isPrime) if val]
        count = 0
        primes = sieve(int(n**0.5 ) + 1)
        for p in primes:
            if p**8<=n:
                count += 1
        length = len(primes)
        for i in range(length):
            for j in range(i+1, length):
                val = (primes[i]**2) * (primes[j]**2)
                if val <=n:
                    count += 1
                else:
                    break
        return count