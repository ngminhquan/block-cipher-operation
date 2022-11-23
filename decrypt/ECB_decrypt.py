import decrypt_aes

#Input
#pt = 'dai hoc bach khoa ha noi'
#cp = '6AFD9025724CECFB672A5354FA37D324BF5D97AF37C51E193C912E7DB1F28C59'
#key = '0f1571c947d9e8590cb7add6af7f6798'
count = 16

with open('input-d.txt', 'r') as cipher,open('output-d.txt', 'w') as text, open('key-d.txt', 'r') as k:
    cp = cipher.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        for i in range(0, len(s), n):
            a.append(s[i:i + n])
        return a

    #decrypt
    def decryptECB(cp, key):
        cp = cp.upper()
        key = key.upper()
        c = divide(cp, 32)
        p = []
        pt = ''
        for i in range(len(c)):
            p.append(decrypt_aes.decrypt(c[i], key))
        for i in range(len(p)):
            pt += p[i]
        pt = pt[:len(pt) - count]
        pt = decrypt_aes.hex_to_text(pt)
        return pt
    pt = decryptECB(cp, key)
    #pt = decrypt_aes.hex_to_text(pt)
    text.write(pt)

#print(decryptECB(cp, key) + '!')
