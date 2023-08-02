## Transposition Cipher

The Transposition Cipher is a simple method of encrypting text by rearranging its characters according to a specific pattern. It operates by permuting the positions of the characters in the original message, making the encrypted message appear scrambled. While it's not as secure as modern encryption techniques, the Transposition Cipher serves as an introduction to the concept of data encryption.

### The steps for encrypting are:
1. Count the number of characters in the message and the key.
2. Draw a number of boxes equal to the key in a single row. (For example, 12 boxes for a
key of 12.)
3. Start filling in the boxes from left to right, with one character per box.
4. When you run out of boxes and still have characters left, add another row of boxes.
98 http://inventwithpython.com/hacking
Email questions to the author: al@inventwithpython.com
5. Shade in the unused boxes in the last row.
6. Starting from the top left and going down, write out the characters. When you get to the
bottom of the column, move to the next column to the right. Skip any shaded boxes. This
will be the ciphertext.

### Example

Let's take a simple example to understand the Transposition Cipher:

- **Original Message:** "HELLO WORLD"
- **Key:** 4

The original message is arranged in a grid with 4 columns:

```
H E L L
O - W O
R L D - 
```
The encrypted message is formed by reading the grid column by column: "HORE LLWDLO ".

### The steps for decrypting are:
1. Calculate the number of columns you will have by taking the length of the message and
dividing by the key, then rounding up.
2. Draw out a number of boxes. The number of columns was calculated in step 1. The
number of rows is the same as the key.
3. Calculate the number of boxes to shade in by taking the number of boxes (this is the
number of rows and columns multiplied) and subtracting the length of the ciphertext
message.
4. Shade in the number of boxes you calculated in step 3 at the bottom of the rightmost
column.
5. Fill in the characters of the ciphertext starting at the top row and going from left to right.
Skip any of the shaded boxes.
6. Get the plaintext by reading from the leftmost column going from top to bottom, and
moving over to the top of the next column

To decrypt, the recipient rearranges the characters into rows again:

```
H O R
E - L
L W D
L O - 
```
The original message "HELLO WORLD" is recovered.

### Usage

1. Install Python on your system.
2. Download this file
3. Run the script using the command: `python transposition.py` in wsl
4. Use can also use online compilers to run the code.

### Write a python script to decrypt transpositon cipher with the key 
### Try without the key deryption also for all keys less than 10.

