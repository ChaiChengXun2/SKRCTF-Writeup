# Fermat's RSA - Cryptography Challenge

## Basic Information
**Name:** Fermat's RSA  
**Category:** Cryptography  
**Points:** 20

## Objective

The "Fermat's RSA" challenge is a cryptography task that involves factoring an RSA modulus using Fermat's factorization method. Your objective is to apply the given formula to find the two prime factors of the modulus and retrieve the hidden flag.

## Solution

To successfully complete the "Fermat's RSA" cryptography challenge, follow these steps:

1. **Use Fermat's Factorization:**
   - In the hints, you are provided with a formula to solve the challenge. This formula is based on Fermat's factorization method, which takes advantage of the fact that the prime factors `p` and `q` in an RSA modulus are very close to each other.

2. **Understanding Fermat's Factorization:**
   - Fermat's factorization is a technique used to factor a composite number `n` into two prime numbers `p` and `q`. The key idea is that if `n` can be expressed as `n = a^2 - b^2`, where `a` and `b` are two integers with `a > b`, then `n` can be factored as `(a + b)(a - b)`.

3. **Apply the Formula:**
   - Using the formula provided in the hints, apply Fermat's factorization to the given modulus. The formula helps you find the values of `a` and `b`, which represent the two prime factors of the modulus.

4. **Formulate an Exploit:**
   - Utilize the values of `a` and `b` obtained from the formula to formulate an exploit. The exploit allows you to factor the modulus and obtain the two prime numbers, which are `p` and `q`.

5. **Flag Discovery:**
   - Once you have successfully factored the modulus and obtained the prime factors `p` and `q`, you can use them to complete the challenge
```python
def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n):
    a = isqrt(n) 
    b2 = a*a - n
    b = isqrt(n) 
    count = 0
    while b*b != b2:
    	print(f"Iteration: {count}")
    	a = a + 1
    	b2 = a*a - n
    	b = isqrt(b2) 
    	count += 1
    p=a+b
    q=a-b
    assert n == p * q
    print(f"P = {p}")
    print(f"Q = {q}")
    return p, q

n=159612650263927599244315225845279212962141958919579628287156052106006464488426972821334606838002857290349373969434861123818942698045862221655834084093326018422357861835363093723358360730673095211096600705379368171946138634823032837497701227361982052478918405795072384781491147017330442761741365938686525436031
fermat(n)
```

Flag: SKR{XXXXXXXXXX}

**Challenge Solved**  
