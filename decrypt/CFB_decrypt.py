import encrypt_aes

#Input
#pt = 'truong dai hoc bach khoa ha noi'
cp = '8B79F125429AC474A17352EE8C20F2976F2DADD90CB8EBCFC4E3BE9AD1F797'
key = '0f1571c947d9e8590cb7add6af7f6798'

#Chia thanh cac khoi 8-bit
def divide(s):
    a = []
    for i in range(0, len(s), 8):
        a.append(s[i:i + 8])
    return a

def decryptCFB(cp, key):
    IV = '0123456789abcdeffedcba9876543210'
    cp = cp.upper()
    key = key.upper()
    IV = IV.upper()
    reg = encrypt_aes.encrypt(IV, key)
    c = divide(cp)
    pt = ''
    p = encrypt_aes.xor_hex(c[0], reg[0:8])
    pt += p
    for i in range(1, len(c)):
        reg = reg[8:] + c[i-1]
        reg = encrypt_aes.encrypt(reg, key)
        p = encrypt_aes.xor_hex(c[i], reg[0:8])
        pt += p
    pt = encrypt_aes.hex_to_text(pt)
    return pt

print(decryptCFB(cp, key) + '!')

