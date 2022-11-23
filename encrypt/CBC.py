import aes

#input
#pt = 'truong dai hoc bach khoa ha noi'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-e.txt', 'r') as text,open('output-e.txt', 'w') as cipher, open('key-e.txt', 'r') as k:
    pt = text.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        count = 0
        for i in range(0, len(s), n):
            a.append(s[i:i + n])
        for i in range(len(a)):
            if len(a[i]) < n:
                a[i] += '8'
                count += 1
                for j in range(0, n):
                    if len(a[i]) == n:
                        break
                    a[i] += '0'
                    count += 1
        return [a, count]

    count = divide(aes.text_to_hex(pt), 32)[1]

    #encrypt CBC
    def encryptCBC(pt, key):
        pt = aes.text_to_hex(pt)
        pt = pt.upper()
        key = key.upper()
        IV = '0123456789abcdeffedcba9876543210'
        IV = IV.upper()
        p = divide(pt, 32)[0]
        pre_c = aes.xor_hex(p[0], IV)
        cr = aes.encrypt(pre_c, key)
        c = []
        c.append(cr)
        cp = ''
        for i in range(1, len(p)):
            pr = aes.xor_hex(p[i], cr)
            cr = aes.encrypt(pr, key)
            c.append(cr)
        for i in range(len(c)):
            cp += c[i]
        return cp
    cp = encryptCBC(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)
    #print(encryptCBC(pt, key))
    #print(count)




