## Affine Cipher:

The Affine Cipher is a type of substitution cipher that combines the features of the Caesar Cipher and the Multiplicative Cipher. It involves using modular arithmetic to transform each letter in the plaintext to create the corresponding ciphertext. The formula for encryption is:

```
E(x) = (ax + b) % m
```

Where:
- `E(x)` is the encrypted letter.
- `x` is the original letter's numerical value.
- `a` and `b` are the key values.
- `m` is the size of the alphabet (usually 26 for English).

### Encryption Process:

1. **Convert to Numerical Values:** Convert each letter in the plaintext to its numerical value using the alphabet order (A=0, B=1, ..., Z=25).

2. **Apply Encryption Formula:** Use the formula `E(x) = (ax + b) % m` to encrypt each numerical value.

3. **Map to Characters:** Convert the encrypted numerical values back to their corresponding characters using the alphabet order.

### Example of Encryption:

**Plaintext:** "HELLO"  
**Key (a, b):** (5, 8)  
**Alphabet Size (m):** 26

1. Convert to Numerical Values:
   - H: 7
   - E: 4
   - L: 11
   - L: 11
   - O: 14

2. Apply Encryption Formula:
   - H: `(5 * 7 + 8) % 26 = 17 -> R`
   - E: `(5 * 4 + 8) % 26 = 2 -> C`
   - L: `(5 * 11 + 8) % 26 = 11 -> L`
   - L: `(5 * 11 + 8) % 26 = 11 -> L`
   - O: `(5 * 14 + 8) % 26 = 0 -> A`

**Encrypted Ciphertext:** "RCLLA"

### Decryption Process:

Decryption in the Affine Cipher involves using the formula `D(x) = a^(-1) * (x - b) % m`, where `a^(-1)` is the modular multiplicative inverse of `a` modulo `m`. This allows us to transform the ciphertext back to the original plaintext.

### Example of Decryption:

**Ciphertext:** "RCLLA"  
**Key (a, b):** (5, 8)  
**Alphabet Size (m):** 26

1. Convert Ciphertext to Numerical Values:
   - R: 17
   - C: 2
   - L: 11
   - L: 11
   - A: 0

2. Calculate Modular Multiplicative Inverse of `a`:
   - In this example, `a = 5`. The modular multiplicative inverse of 5 modulo 26 is 21.

3. Apply Decryption Formula:
   - R: `21 * (17 - 8) % 26 = 7 -> H`
   - C: `21 * (2 - 8) % 26 = 4 -> E`
   - L: `21 * (11 - 8) % 26 = 11 -> L`
   - L: `21 * (11 - 8) % 26 = 11 -> L`
   - A: `21 * (0 - 8) % 26 = 14 -> O`

**Decrypted Plaintext:** "HELLO"

### Security and Limitations:

The security of the Affine Cipher depends on the choice of key values `a` and `b`. If `a` is not coprime with the alphabet size `m`, then some letters may not be reversible, reducing the possible keys. The Affine Cipher is relatively weak against modern cryptanalysis techniques, especially with larger alphabets.

#### Write a Brute force decryption algorithm by yourself