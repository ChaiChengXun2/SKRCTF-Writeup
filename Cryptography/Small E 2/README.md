# Small-E 2 - Cryptography Challenge

## Basic Information
**Name:** Small-E 2  
**Category:** Cryptography  
**Points:** 346

## Objective

The "Small-E 2" challenge is a cryptography task, similar to its predecessor. It requires knowledge of RSA encryption and how to reverse a modulus equation. Your objective is to decrypt a given ciphertext (c) to find the original message (m) and reveal the hidden flag.

## Solution

To successfully complete the "Small-E 2" cryptography challenge, follow these steps:

1. **Understanding the RSA Modulus Equation:**
   - In RSA encryption, the modulus equation is typically represented as: `c = m^e mod n`, where `c` is the ciphertext, `m` is the message, `e` is the public exponent, and `n` is the modulus. The challenge requires reversing this equation to find `m`.

2. **Modulus Equation Reversal (c = m mod n):**
   - To reverse the modulus equation (`c = m mod n`), you can represent it as `m = tn + c`, where `t` is an integer. The goal is to find the original message `m`.

3. **Python Script for Automation:**
   - As before, you can write a Python script to automate the process of reversing the modulus equation. The script should loop through all possible values of `t` to find the message `m` that satisfies the modulus equation.

4. **Root of E (m is a true root of e):**
   - Just like in the previous challenge, the key to finding the correct message is when the message `m` is a true root of `e`, meaning that `m^e mod n` equals the given ciphertext `c`. This is the moment when you've successfully decrypted the message.
```python
import gmpy2 

n=91916062929755899991419452098776070211257414596875218275380603377591870182603435387592799597601677412725463330022618304491967226095274532701595395513081487786880774375261242719962843053332094817389705801521607097644046054957895718424075514672164946208067840011762933432075645942010887315772486354077753098921
e=5
c=35783243553484273090677089927059990920007599084499143586613182895028518498096602289698991044152216674632952484103049422671044257404009588038522559515118720479025871564218557941067601815602070912535220611164761904849438827907551620715608094645194620571566118891025017218047159723272277310954299826359459603893

for t in range(1000):
	m, is_true_root = gmpy2.iroot(t * n + c, e)
	if is_true_root:
		print(bytearray.fromhex(format(m, "x")).decode())
```

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
