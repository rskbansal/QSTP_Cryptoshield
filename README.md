# QSTP_Cryptoshield
All the resources, assignments and code snippets from Cryptoshield, A Quark Summer Term Project 2023, BITS Goa

## Some common tools to lookout for
- [dCode](https://www.dcode.fr/)
- [Cryptii](https://cryptii.com/)
- [Esolangs](https://esolangs.org/wiki/Main_Page)
- [Boxentriq](https://www.boxentriq.com/code-breaking)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Try It Online](https://tio.run/)

### Reversed Text
Sometimes a ***ciphertext*** is just as easy as reversed text. Don't forgot to check under this rock!<br><br>
You can reverse a string using a simple Bash script:
```bash
echo string | rev
```
Or using Python:
```python
ct = "string"
print(ct[::-1])
```

### Brainfuck


Here are the eight Brainfuck commands:

| Command | Description                                          |
|---------|------------------------------------------------------|
| `>`     | Increment the memory pointer (move to the right)   |
| `<`     | Decrement the memory pointer (move to the left)    |
| `+`     | Increment the value at the current memory cell     |
| `-`     | Decrement the value at the current memory cell     |
| `[`     | Jump forward to the command after matching `]` if the value at the current cell is zero |
| `]`     | Jump back to the command after matching `[` if the value at the current cell is nonzero |
| `,`     | Read a single character from input and store it in the current memory cell |
| `.`     | Output the character at the current memory cell    |

Each command operates on a simple memory model, and Brainfuck programs are composed of sequences of these commands to perform computations and execute algorithms.

https://tio.run/#brainfuck

### Base64
Base64 is a group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding.<br><br>
It's primarily used for situations where binary data needs to be transmitted or stored as text, such as in email attachments, URLs, or configuration files. Base64 is not an encryption method; rather, it's a way to represent binary data in a format that is safe for text-based systems.

Here's a detailed explanation of Base64:

#### Basics of Encoding:

1. **Character Set:** Base64 uses a set of 64 different characters (hence the name). These characters consist of letters (uppercase and lowercase), digits, and two additional symbols.

2. **3 Bytes Mapping:** Base64 encodes binary data in groups of 3 bytes (24 bits) at a time. Each group of 3 bytes is then split into four 6-bit chunks.

3. **Encoding Table:** Base64 uses an encoding table that assigns each possible 6-bit value to a specific character. The table is the foundation for the conversion from binary to text.

#### Encoding Process:

1. **Binary Data:** The input binary data is divided into groups of 3 bytes (24 bits).

2. **Dividing into 6-Bit Chunks:** Each 3-byte group is divided into four 6-bit chunks. If the binary data length is not a multiple of 3, padding is added to make it a multiple of 3 bytes.

3. **Mapping to Characters:** Each 6-bit chunk is mapped to its corresponding character in the Base64 encoding table.

4. **Padding:** If the input data is not a multiple of 3 bytes, padding is added to the end of the encoded data to ensure that the last chunk is properly formed.

#### Example:

Let's encode the ASCII string "Hello" using Base64:

1. **String:** "Hello"
2. **ASCII Values:** 72 101 108 108 111
3. **Binary:** 01001000 01100101 01101100 01101100 01101111

Divide the binary data into 6-bit chunks:

- 010010 000110 010101 101100 110011 011011 000110 110011 011011 011110
- Decimal: 18 6 21 44 51 27 6 51 27 30

Map the decimal values to Base64 characters:

- 18: S
- 6: G
- 21: V
- 44: s
- 51: z
- 27: H
- 6: G
- 51: z
- 27: H
- 30: e

Encoded Base64: "SGVsbG8="

#### Decoding:

Decoding Base64 is the reverse process. Each character is mapped back to its 6-bit value, and then these values are combined to retrieve the original binary data.

#### Key Points:

- Base64 doesn't provide encryption; it's meant for data representation.
- Base64 encoding increases the size of data by about 33%.
- URLs often use Base64 encoding to safely include binary data.
- Base64 is commonly used in email systems for attaching images and files.

In summary, Base64 is a mechanism to represent binary data using a limited set of characters, making it suitable for text-based environments. It's essential when binary data needs to be included in systems that only support text.


### Atbash Cipher
The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed i.e. all A's are replaced with Z's, all B's are replaced with Y's, and so on. It was originally used for the Hebrew alphabet, but can be used for any alphabet system.<br><br>
You can use the following tools to encrypt/decrypt using the Atbash cipher:

- [Cryptii](https://cryptii.com/pipes/atbash-cipher)
- [dCode](https://www.dcode.fr/atbash-cipher)

### Malbolge
An esoteric language that looks a lot like Base85, but isn't.<br><br>
Use these interpreters:

- [Malbolge Tools](http://zb3.me/malbolge-tools/)
- [Malbolge - interpreter online](https://malbolge.doleczek.pl/)

```
(=<`#9]~6ZY32Vx/4Rs+0No-&Jk)"Fh}|Bcy?`=*z]Kw%oG4UUS0/@-ejc(:'8dc
```
Translates to - `Hello World!`

### Rockstar
A language intended to look like a song's lyrics, heavily influenced by the lyrical conventions of 1980s hard rock and power ballads. [GitHub Repository](https://github.com/RockstarLang/rockstar)<br><br>
You can use their official online interpreter - https://codewithrockstar.com/online
