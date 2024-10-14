#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        # Create a boolean array "prime[0..n]" and initialize all entries as true.
        # A value in prime[i] will be False if i is Not a prime, True if it is a prime.
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        p = 2
        while (p * p <= n):
            # If prime[p] is not changed, then it is a prime
            if primes[p] == True:
                # Updating all multiples of p to False, as they are not primes
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    # We calculate the prime numbers once up to the largest n in nums
    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)

    # Count how many primes are <= n for each round
    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if prime_flags[i]:
            count += 1
        prime_counts[i] = count

    # Now we play x rounds, one for each n in nums
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes up to n is odd, Maria wins (because she goes first)
        # If the number of primes is even, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the winner of most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
