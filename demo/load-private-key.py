import icrypto 

encryted_private_key = "b0b9fd4136dea8a64e0f1970b22dc69c54384b86f80541fee2a99d8372ab8e2f2b4df0b5cf57c14cedcfff9986bc53f18459cdec05f748865d906d73a61dc81b01"

# Decrypt a string
decrypted = icrypto.decrypt(encryted_private_key)
print('Decrypted:', decrypted)

