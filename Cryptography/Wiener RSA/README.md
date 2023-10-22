# Wiener's RSA - Cryptography Challenge

## Basic Information
**Name:** Wiener's RSA  
**Category:** Cryptography  
**Points:** 20

## Objective

The "Wiener's RSA" challenge is a cryptography task that requires applying Wiener's algorithm to find the private key for an RSA encryption when `n` and `e` are given. Your objective is to use the provided formula and a Python script to solve the challenge and retrieve the hidden flag.

## Solution

To successfully complete the "Wiener's RSA" cryptography challenge, follow these steps:

1. **Utilize Wiener's Algorithm:**
   - From the challenge name, you are given the formula required, which is Wiener's algorithm. Wiener's algorithm is used to find the private key `d` in an RSA encryption when you have `n` and `e` values.

2. **Understanding Wiener's Algorithm:**
   - Wiener's algorithm is an approach used to factor the modulus `n` and find the private key `d` in an RSA encryption when the public exponent `e` is small compared to `n`. The algorithm takes advantage of the fact that `d` is very close to `e/n`.

3. **Flag Discovery:**
   - Once you have the private key `d`, you can submit it as a flag.

```python
import math
import random

def main():
  e = 0x4bbae571725f342aa8e86759a02d7c1e9edcf334827630e34763492b1773d6df00f74d8bf14c4de34f1cf7c9d7e1c297c83df9f2f2c1a74eeaeb3952f7392edd4fda4e62611cca4e5633f682d6056745e2e9f45cfd842a17bac72b91f65d64df9229b45c4a70ebbff70f5049b6752dfaf87050ad12b872fa4e1e37b5784b02188c4df6601a8b182f0457d1bce249f8930255bac8e6c6b3c5d92de6389f9b818a631657fdb61e98c4ca14642bb3599fa86cbe020d5983aa5f3c1d40df75ffa323a0d6be883ee80e7b89fdb1c2c66b04befd6be324cbf997b7732ebe7f36e0de4311562547ed2b234bb8613e3f4b41cb8b7e180762c341edf298c4a78e81879779
  n = 0xa8d62e71dc2baad2c8d8b4eae7837c07505dcdadf476ccbf51357e5204807eff3d5234193b40dd69c69a24f6b135b267a7616ed5aec4959f9e09056ff2875b489905519039316f906727dfcedc6e7de3a1bf5f06653378deb80c0796d6a2d3f54c1130696ad3d631739cb708aeadb6e5afea7cc8f772c3b89eb4a62fdd71b93e20b4441189233bcb7b80a1538e9fa2036691aa232b7400355b745a84057fa400c28c17b22c0ea681a6ae8b3d03da81978edcca6750080c103d0639270d0742fe3f1bc20d82e7855c876f06436ba85a9bdc6ca5378fdcb496d2a4a2186564355379e9abc42dbfed78710a201393ac2cf351b28c10d1ea9000d0f0e9451980758b
  p, q, d = wiener_attack(n, e)
  print(d)

def bitlength(x):
  assert x >= 0
  n = 0
  while x > 0:
    n = n + 1
    x = x >> 1
  return n

def isqrt(n):
  if n < 0:
    raise ValueError('square root not defined for negative numbers')
  if n == 0:
    return 0
  a, b = divmod(bitlength(n), 2)
  x = 2**(a + b)
  while True:
    y = (x + n // x) // 2
    if y >= x:
      return x
    x = y

def is_perfect_square(n):
  h = n & 0xF  
  if h > 9:
    return -1 
  if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
    t = isqrt(n)
    if t * t == n:
      return t
    else:
      return -1
  return -1

def partial_quotients(x, y):
  partials = []
  while x != 1:
    partials.append(x // y)
    a = y
    b = x % y
    x = a
    y = b
  return partials

def indexed_convergent(sequence):
  i = len(sequence) - 1
  num = sequence[i]
  denom = 1
  while i > 0:
    i -= 1
    a = (sequence[i] * num) + denom
    b = num
    num = a
    denom = b
  return (num, denom)

def convergents(sequence):
  c = []
  for i in range(1, len(sequence)):
    c.append(indexed_convergent(sequence[0:i]))
  return c

def phiN(e, d, k):
    return ((e * d) - 1) // k

def wiener_attack(N, e):
  p, q, d = (0, 0, 0)
  conv = convergents(partial_quotients(e, N))
  for frac in conv:
    k, d = frac
    if k == 0:
      continue
    y = -(N - phiN(e, d, k) + 1)
    discr = y * y - 4 * N
    if discr >= 0:
      sqr_discr = is_perfect_square(discr)
      if sqr_discr != -1 and (-y + sqr_discr) % 2 == 0:
        p = ((-y + sqr_discr) // 2)
        q = ((-y - sqr_discr) // 2)
        return p, q, d
  return p, q, d

main()

```

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
