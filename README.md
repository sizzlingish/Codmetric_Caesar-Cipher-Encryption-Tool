# 🔐 Caesar Cipher Encryption & Decryption Tool

## Overview

The **Caesar Cipher Encryption & Decryption Tool** is a Python application that demonstrates one of the earliest and simplest encryption techniques in cryptography. It allows users to encrypt and decrypt text using a user-defined shift value while preserving spaces, numbers, and punctuation.

The project also includes a brute-force decryption feature, enabling users to see how easily a Caesar Cipher can be broken by trying all possible shift values. An educational section explains how the cipher works and why it is considered insecure by modern security standards.

This project was developed as part of a Cybersecurity Internship to introduce classical cryptography concepts, cryptanalysis, and secure programming practices.

---

## Features

* Encrypt text using the Caesar Cipher
* Decrypt encrypted text using a shift value
* Brute-force decryption (tries all 25 possible shifts)
* Learn About Caesar Cipher section
* Read text from keyboard or a text file
* Save encrypted or decrypted output to a file
* User-friendly console interface
* Input validation
* Error handling
* Supports uppercase letters, lowercase letters, numbers, spaces, and punctuation

---

## Technologies Used

* Python 3
* `os`

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/caesar-cipher-tool.git
```

2. Navigate to the project folder:

```bash
cd caesar-cipher-tool
```

3. Run the program:

```bash
python caesar_cipher.py
```

---

## Example

```text
============================================================
        🔐 CAESAR CIPHER ENCRYPTION TOOL
============================================================

1. Encrypt Text
2. Decrypt Text
3. Brute Force Decryption
4. Learn About Caesar Cipher
5. Exit
```

### Encryption Example

```text
Original Text

HELLO WORLD

Shift Value

3

Encrypted Text

KHOOR ZRUOG
```

### Brute Force Example

```text
Shift 1 : JGNNQ YQTNF
Shift 2 : IFMMP XPSME
Shift 3 : HELLO WORLD  <-- Most Likely
...
Shift 25 : LIPPS ASVPH
```

---

## How It Works

### Encryption

Each alphabet letter is shifted forward by a fixed number of positions.

Example:

```text
HELLO

↓

KHOOR (Shift = 3)
```

### Decryption

The encrypted text is shifted backward using the same shift value to recover the original message.

### Brute Force Decryption

The program attempts every possible shift value (1–25) and displays all possible decrypted messages. Since the Caesar Cipher has only 25 possible keys, it can be broken easily using this technique.

---

## Learning Outcomes

This project helped me understand:

* Classical cryptography
* Caesar Cipher algorithm
* Encryption and decryption techniques
* Basic cryptanalysis using brute-force attacks
* File handling in Python
* User input validation
* Exception handling
* Modular programming using functions
* Building user-friendly console applications

---

## Limitations

The Caesar Cipher is **not secure** for protecting sensitive information because:

* It has only 25 possible shift values.
* It is vulnerable to brute-force attacks.
* It provides very little resistance against modern cryptanalysis.

Modern encryption algorithms such as **AES** and **RSA** are significantly more secure.

---

## Notes

* This project is intended for educational purposes only.
* It demonstrates the principles of classical encryption rather than modern cryptographic security.
* Numbers, spaces, and punctuation remain unchanged during encryption and decryption.

---

## Author

Developed by **Areeba** as part of a Cybersecurity Internship.
