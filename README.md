# icrypto
A simple encryption and decryption module with password-based encryption.

## Description
This module provides a simple symestric encryption and decryption function.
Usually, we use the cryptography module to encrypt and decrypt data. 
However, the cryptography module is a bit complicated to use. 
This module is a simple wrapper for the cryptography module.
It provide a password-based (getpass module) encryption and decryption function.

## Supported Algorithms
- AES
- DES (Ready)
- DES3 (Ready)
- Blowfish (Ready)
- Camellia (Ready)


## Installation
```bash
pip install icrypto
```

## Usage

```python
# case1
import icrypto 

# Encrypt a string
text="Hello World"
encrypted = icrypto.encrypt(text, algorithm='AES')
print('Encrypted:', encrypted)

# Decrypt a string
decrypted = icrypto.decrypt(encrypted)
print('Decrypted:', decrypted)


# case2
import icrypto 

encryted_private_key = "b0b9fd4136dea8a64e0f1970b22dc69c54384b86f80541fee2a99d8372ab8e2f2b4df0b5cf57c14cedcfff9986bc53f18459cdec05f748865d906d73a61dc81b01"

# Decrypt a string
decrypted = icrypto.decrypt(encryted_private_key)
print('Decrypted:', decrypted)

```

## License
MIT
