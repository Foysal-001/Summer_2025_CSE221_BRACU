"""
Algorithm: Prime Factorization using Trial Division (Optimized)
What Does It Do?
-----------------
This algorithm finds **all prime factors** of a single number
`n`, including repeated factors.
Example: For n = 60 → Output: 2 2 3 5


What Are We Replacing?
------------------------
This replaces the **naive/brute-force** approach, where you:
- Check every number from 2 up to n to see if it divides n.
- That method has **O(n)** time complexity and is **extremely slow** 
- for large n (e.g., n = 10^9 or more).


More optimized version
-------------------------------
- Instead of going up to n, we only go up to √n.
- We first divide out all 2s to handle even numbers quickly.
- Then, we check only **odd numbers** (since even ones are already handled).
- If any number remains > 1, it must be a prime (no need to check further).



Time & Space Complexity:
-------------------------
- **Time Complexity:** O(√n)
  (Much faster than the naive O(n) method)
- **Space Complexity:** O(log n) in worst case for storing prime factors

"""

import sys
input = sys.stdin.readline

n = int(input())
factors = []
while n % 2 == 0:
    factors.append(2)
    n //= 2
i = 3
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 2
if n > 1:
    factors.append(n)
print(*factors)

