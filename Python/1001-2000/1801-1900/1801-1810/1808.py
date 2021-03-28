class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        mod = 1_000_000_007
        if primeFactors <= 3:
            return primeFactors
        elif primeFactors % 3 == 0:
            return pow(3, primeFactors//3, mod)
        elif primeFactors % 3 == 1:
            return 4*pow(3, (primeFactors-4)//3, mod) % mod
        else:
            return 2*pow(3, primeFactors//3, mod) % mod
