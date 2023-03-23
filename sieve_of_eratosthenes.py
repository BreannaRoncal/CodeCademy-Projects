"""
The Sieve of Eratosthenes

The sieve provides a set of steps for finding all prime numbers up to a given
limit. In this article, we’ll cover implementing the Sieve of Eratosthenes in
Python. As a reminder, a prime number is a positive number with no divisors
but 1 and itself. 2, 3, 11, and 443 are all prime numbers.


    1. Create a list of all integers from 2 to n.
    2. Start with the smallest number in the list (2, the smallest prime number).
    3. Mark all multiples of that number up to n as not prime.
    4. Move to the next non-marked number and repeat this process until the
       entire list has been covered.
       
"""


def sieve_of_eratosthenes(limit):
  true_indices = []
  # Check that limit is valid
  if limit <= 1:
    return true_indices

  output = [True] * (limit + 1)
  output[0] = False
  output[1] = False

  for i in range(2, limit + 1):
    if output[i] == True:
      j = i * 2
      while j <= limit:
        output[j] = False
        j += i
  true_indices = [i for (i, v) in list(enumerate(output)) if v == True]
  return true_indices


primes = sieve_of_eratosthenes(13)
print(primes) # should return [2, 3, 5, 7, 11, 13]
