import encrypt_aes

#input
#pt = 'dai hoc bach khoa ha noi he thong nhung iot'
cp = '9B6AED6A603CDC5C0B55C82B447FE7D69764392B4A8ABDEF07606DB07D20E132FA60BAF74FEB1249B5A867'
key = '0f1571c947d9e8590cb7add6af7f6798'

#Chia thanh cac khoi n-byte (8*n-bit)
def divide(s, n):
    a = []
    for i in range(0, len(s), n):           #Chia thanh cac khoi n-bit
        a.append(s[i:i + n])                ##khoi cuoi < n-bit khong padding
    return a

def decryptOFB(cp, key):
    nonce = '0123456789abcdeffedcba9876543210'
    cp = cp.upper()
    key = key.upper()
    nonce = nonce.upper()
    out = nonce
    c = divide(cp, 32)
    pt = ''
    for i in range(len(c)):
        if i == len(c) - 1:
            out = encrypt_aes.encrypt(out, key)
            p = encrypt_aes.xor_hex(out[:len(c[i])], c[i])
            pt += p
            break
        out = encrypt_aes.encrypt(out, key)
        p = encrypt_aes.xor_hex(c[i], out)
        pt += p
    pt = encrypt_aes.hex_to_text(pt)
    return pt

print(decryptOFB(cp, key) + '!')
