import aes

#Input
#pt = 'dai hoc bach khoa ha noi'
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
    #Encrypt ECB
    def encryptECB(pt, key):
        pt = aes.text_to_hex(pt)
        pt = pt.upper()
        key = key.upper()
        p = divide(pt, 32)[0]
        c = []
        cp = ''
        for i in range(len(p)):
            c.append(aes.encrypt(p[i], key))
        for i in range(len(c)):
            cp += c[i]
        return cp
    cp = encryptECB(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)

#print(encryptECB(pt, key))
#print(count)


