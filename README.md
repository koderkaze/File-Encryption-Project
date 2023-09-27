# File-Encryption-Project

# File Encryptor

## Overview

The File Encryptor is a simple Python-based command-line tool that enables users to secure sensitive data by encrypting files. This project uses the `cryptography` library to implement encryption and decryption functionalities, providing a straightforward way to protect and recover data.

## Features

- **User-Friendly Interface:** The program offers a user-friendly command-line interface with a menu system that allows users to choose between file encryption and decryption.

- **Encryption and Decryption:** The File Encryptor program successfully implements encryption and decryption functions, ensuring data security and recoverability.

- **Key Generation and Management:** Integrated key generation and management functionalities for secure encryption and decryption processes. **Key expires/deletes after 90 days so beware!**

- **Error Handling:** Robust error handling is in place to handle various scenarios, including file existence checks and user input validation.

## Usage

1. **Encryption:**
   - To encrypt a file, run the program and choose option 1.
   - You will be prompted to enter the path of the file you want to encrypt.
   - The program will generate an encryption key and store it securely, if one does not already exist.
   - The encrypted file will be saved with a ".enc" extension in the same directory.

2. **Decryption:**
   - To decrypt an encrypted file, run the program and choose option 2.
   - Enter the path of the encrypted file you want to decrypt.
   - The program will use the stored encryption key to decrypt the file.
   - The decrypted content will be saved with the original filename.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/file-encryptor.git
   ```

2. Install the required dependencies:
   ```
   pip install cryptography
   ```

3. Run the program:
   ```
   python FileEncryptionProject.py
   ```

## Author

- [Koderkaze](https://github.com/koderkaze)


## Acknowledgments

- [Cryptography Library](https://cryptography.io/en/latest/): Used for implementing encryption and decryption.
- [Python](https://www.python.org/): The programming language used for this project.
