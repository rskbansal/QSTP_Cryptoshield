## Transposition Cipher

The Transposition Cipher is a simple method of encrypting text by rearranging its characters according to a specific pattern. It operates by permuting the positions of the characters in the original message, making the encrypted message appear scrambled. While it's not as secure as modern encryption techniques, the Transposition Cipher serves as an introduction to the concept of data encryption.

### How It Works

1. **Choosing a Key:** The key is a number that determines the pattern for rearranging the characters. The recipient needs to know the key to decrypt the message.

2. **Creating Columns:** The message is written out in a grid with a fixed number of columns determined by the key. Each character occupies a cell in the grid.

3. **Reading Columns:** The encrypted message is formed by reading the grid column by column. The characters are extracted from each column to create the encrypted text.

4. **Decryption:** To decrypt the message, the recipient uses the same key and arranges the characters back into rows. The original message is recovered by reading across the rows.

### Example

Let's take a simple example to understand the Transposition Cipher:

- **Original Message:** "HELLO WORLD"
- **Key:** 4

The original message is arranged in a grid with 4 columns:

