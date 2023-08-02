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