import aes

#input
pt = 'dai hoc bach khoa ha noi'
key = '0f1571c947d9e8590cb7add6af7f6798'

#Chia thanh cac khoi n-byte (8*n-bit)
def divide(s, n):
    a = []
    for i in range(0, len(s), n):
        a.append(s[i:i + n])
    for i in range(len(a)):
        if len(a[i]) < n:
            a[i] += '8'
            for j in range(0, n):
                if len(a[i]) == n:
                    break
                a[i] += '0'
    return a

#encrypt CBC
def encryptCBC(pt, key):
    pt = aes.text_to_hex(pt)
    pt = pt.upper()
    key = key.upper()
    IV = '0123456789abcdeffedcba9876543210'
    IV = IV.upper()
    p = divide(pt, 32)
    #print('p la: ', p)
    pre_p = aes.xor_hex(p[0], IV)
    cr = aes.encrypt(pre_p, key)
    c = []
    c.append(cr)
    cp = ''
    for i in range(1, len(p)):
        pr = aes.xor_hex(p[i], cr)
        cr = aes.encrypt(pr, key)
        c.append(cr)
        #print('pr la: ', pr)
        #print('cr la: ', cr)
    for i in range(len(c)):
        cp += c[i]
    return cp

print(encryptCBC(pt, key))




