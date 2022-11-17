import aes

#input
pt = 'dai hoc bach khoa ha noi he thong nhung iot'
key = '0f1571c947d9e8590cb7add6af7f6798'

#Chia thanh cac khoi n-byte (8*n-bit)
def divide(s, n):
    a = []
    for i in range(0, len(s), n):           #Chia thanh cac khoi n-bit
        a.append(s[i:i + n])                ##khoi cuoi < n-bit khong padding
    return a

#Encrypt
def encryptOFB(pt, key):
    nonce = '0123456789abcdeffedcba9876543210'
    pt = aes.text_to_hex(pt)
    pt = pt.upper()
    key = key.upper()
    nonce = nonce.upper()
    out = nonce
    p = divide(pt, 32)
    cp = ''
    for i in range(len(p)):
        if i == len(p) - 1:
            out = aes.encrypt(out, key)
            c = aes.xor_hex(out[:len(p[i])], p[i])
            cp += c
            break
        out = aes.encrypt(out, key)
        c = aes.xor_hex(p[i], out)
        cp += c
    return cp

print(encryptOFB(pt, key))








