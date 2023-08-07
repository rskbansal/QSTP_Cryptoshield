# Too-Based
## Question 1
### Description
The mentors of QSTP, just broke 'QSTP' into 2 words and created a cipher out of it. But they don't really remember how to decode it & hence, asks your help to get back the original message. Let's see how devotedly, you attended the sessions  : )

[Ciphertext](./1.txt)

### Solution
There are only QSs & TPs, which hints for some 2-character encryption. Also, each of the rows have 8 such strings in total & all of them begins with `QS`. This hints that this is a simple binary encryption with `QS->0` & `TP->1`. Use any online binary to text converter to get the flag.

[Tool](https://codebeautify.org/remove-punctuation)

### Flag
```
QSTP{8in4ry_i5_fUn!}
```


## Question 2
### Description
This weird string with dots & dashes looks like a method to encode text in telecommunication. Your task is to understand what it could possibly mean. However, be cautious of potential distractions or misleading sequences that could lead you astray  0_0

[Ciphertext](./2.txt)

### Solution
The description hints towards morse code but it seems to be incorrect. Also, in the latter part of the question it warns us not to fall for traps. As it contains only dots and dashes. Replacing `- with 0` & `. with 1` gives us a binary string. Converting it to text gives us the flag.

[Tool](https://codebeautify.org/remove-punctuation)

### Flag
```
QSTP{5icK_0f_B1nary_nOw_:(}
```


## Question 3
### Description
My friend used a very known encryption to send me a piece of text over the internet in a secure way. However, 5 of my colleagues at BITSkrieg intercepted the message in between one after the other. Instead of decrypting the ciphertext, they further encrypted it using the same encryption.

[Ciphertext](./3.txt)

### Solution
Looking at the ciphertext, it seems clear that the piece of text is encoded with binary but it looks huge & hence, maybe encoded multiple times. Reading the description, it seems it was done `5+1=6` times. We can use **CyberChef** to decode it as the file is pretty big & can't be handled by other tools. We can also use a Python script to deal with even bigger files.

- [CyberChef Recipe](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)From_Binary('Space',8)From_Binary('Space',8)From_Binary('Space',8)From_Binary('Space',8)From_Binary('Space',8))
- [Python Script](./dec.py)

### Flag
```
QSTP{FUcCk_b1nary!?}
```
> **Note**
> I used [this](./gen.py) script to generate the ciphertext