# File Encryption Tool

This project provides a simple tool to encrypt and decrypt files using a symmetric key. The tool consists of two scripts:

generate_key.py: Generates a symmetric encryption key and saves it to a file.
crypto_tool.py: Encrypts and decrypts files using the generated key.

## Features

- Generate a symmetric encryption key and save it to a file.
- Encrypt files using the generated key.
- Decrypt encrypted files using the generated key.
- Command-line interface for easy usage

## Requirements

- Python 3.x
- `cryptography` library

## Example 

Generate and encrypt key:
python generate_key.py
Key saved to secret.key

python crypto_tool.py encrypt myfile.txt --key secret.key
Encrypted 'myfile.txt' as 'myfile.txt.encrypted'

Decrypt key:
python crypto_tool.py decrypt myfile.txt.encrypted --key secret.key
Decrypted 'myfile.txt.encrypted' back to 'myfile.txt'

## Limitations

- Key Management: The key file (secret.key) must be securely managed. If the key is lost, the encrypted files cannot be decrypted.
- File Size: The tool reads the entire file into memory for encryption and decryption, which may not be suitable for very large files.
- File Overwrite: The tool does not check if the destination file exists. Running the tool multiple times can overwrite existing files without warning.
- Error Handling: Basic error handling is implemented, but the tool may not handle all edge cases gracefully.