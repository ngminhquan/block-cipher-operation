import encrypt_aes

#Input
#pt = 'truong dai hoc bach khoa ha noi'
#cp = '8BF00825E78895F7DC0A8CD28F67D62C5C13F82B5E390F45DC837E917B5D0A'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-d.txt', 'r') as cipher,open('output-d.txt', 'w') as text, open('key-d.txt', 'r') as k:
    cp = cipher.read()
    key = k.read()
    #Chia thanh cac khoi 8-bit
    def divide(s):
        a = []
        for i in range(0, len(s), 2):
            a.append(s[i:i + 2])
        return a

    def decryptCFB(cp, key):
        IV = '0123456789abcdeffedcba9876543210'
        cp = cp.upper()
        key = key.upper()
        IV = IV.upper()
        reg = encrypt_aes.encrypt(IV, key)
        c = divide(cp)
        pt = ''
        p = encrypt_aes.xor_hex(c[0], reg[0:2])
        pt += p
        for i in range(1, len(c)):
            reg = reg[2:] + c[i-1]
            reg = encrypt_aes.encrypt(reg, key)
            p = encrypt_aes.xor_hex(c[i], reg[0:2])
            pt += p
        pt = encrypt_aes.hex_to_text(pt)
        return pt
    pt = decryptCFB(cp, key)
    #pt = decrypt_aes.hex_to_text(pt)
    text.write(pt)

#print(decryptCFB(cp, key) + '!')

