# Small-E - Cryptography Challenge

## Basic Information
**Name:** Small-E  
**Category:** Cryptography  
**Points:** 20

## Objective

The "Small-E" challenge is a cryptography task that requires some knowledge of how RSA encryption works and how to reverse a modulus equation. Your objective is to decrypt a given ciphertext (c) to find the original message (m) and reveal the hidden flag.

## Solution

To successfully complete the "Small-E" cryptography challenge, follow these steps:

1. **Understanding the RSA Modulus Equation:**
   - In RSA encryption, the modulus equation is typically represented as: `c = m^e mod n`, where `c` is the ciphertext, `m` is the message, `e` is the public exponent, and `n` is the modulus. The challenge requires reversing this equation to find `m`.

2. **Modulus Equation Reversal (c = m mod n):**
   - To reverse the modulus equation (`c = m mod n`), you can represent it as `m = tn + c`, where `t` is an integer. The goal is to find the original message `m`.

3. **Python Script for Automation:**
   - To automate the process of reversing the modulus equation, you can write a Python script. The script should loop through all possible values of `t` to find the message `m` that satisfies the modulus equation.

4. **Root of E (m is a true root of e):**
   - The key to finding the correct message is when the message `m` is a true root of `e`, which means that `m^e mod n` equals the given ciphertext `c`. This is the moment when you've successfully decrypted the message.

```python
import gmpy2

n=91401655596661773066154930780102428385236855004133210729170159798059723053894336867560347131631952332857718383766118221054743660000104054380881409954672459759905364040450222929481206116665010512840607309735484651457322640684656804214747214675891230694109905235328054635184004465834580499758589565987517821531
e=3
c=4821735227044737729172894050832578813733965898452420107360773622174975905446542522417312328623823461

for t in range(10):
	m, is_true_root = gmpy2.iroot(t * n + c, e)
	if is_true_root:
		print(bytearray.fromhex(format(m, "x")).decode())
```

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
