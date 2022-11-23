import aes

#input
#pt = 'dai hoc bach khoa ha noi he thong nhung iot'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-e.txt', 'r') as text,open('output-e.txt', 'w') as cipher, open('key-e.txt', 'r') as k:
    pt = text.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        for i in range(0, len(s), n):           #Chia thanh cac khoi n-bit
            a.append(s[i:i + n])                ##khoi cuoi < n-bit khong padding
        return a

    #Encrypt
    def encryptCTR(pt, key):
        ctr = '0123456789abcdeffedcba9876543210'
        pt = aes.text_to_hex(pt)
        pt = pt.upper()
        key = key.upper()
        ctr = ctr.upper()
        p = divide(pt, 32)
        out_ctr = ctr
        cp = ''
        for i in range(len(p)):
            if i == len(p) - 1:
                out_ctr = aes.encrypt(out_ctr, key)
                c = aes.xor_hex(out_ctr[:len(p[i])], p[i])
                cp += c
                break
            out_ctr = aes.encrypt(out_ctr, key)
            c = aes.xor_hex(p[i], out_ctr)
            cp += c
            out_ctr = aes.add_hex(out_ctr, '1')
        return cp
    cp = encryptCTR(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)

#print(encryptCTR(pt, key))
