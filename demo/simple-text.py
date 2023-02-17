import icrypto 

# Encrypt a string
text="Hello World"
encrypted = icrypto.encrypt(text)
print('Encrypted:', encrypted)

# Decrypt a string
decrypted = icrypto.decrypt(encrypted)
print('Decrypted:', decrypted)