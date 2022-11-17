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

#counter


#Encrypt
def encryptCTR(pt, key):
    ctr = '0123456789abcdeffedcba9876543210'
    pt = aes.text_to_hex(pt)
    pt = pt.upper()
    key = key.upper()
