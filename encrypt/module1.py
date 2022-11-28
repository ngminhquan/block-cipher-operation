import numpy as np
from PIL import Image
import aes
#img = Image.open('anhtest.jpg')
#img.show()
img = Image.open('testanh.jpg')
key = '0f1571c947d9e8590cb7add6af7f6798'

def encryptCFB(pt, key):
        IV = '0123456789abcdeffedcba9876543210'
        pt = pt.upper()
        key = key.upper()
        IV = IV.upper()
        reg = aes.encrypt(IV, key)
        p = aes.divide(pt, 2)
        cp = ''
        c = aes.xor_hex(p[0], reg[0:2])
        cp += c
        for i in range(1, len(p)):
            reg = reg[2:] + c
            reg = aes.encrypt(reg, key)
            c = aes.xor_hex(p[i], reg[0:2])
            cp += c
        return cp

def bin_img(img):
    #tạo ảnh mới giống ảnh nhập vào
    binimg = Image.new(img.mode, img.size)

    #lấy kích thước của ảnh
    width = binimg.size[0]
    height = binimg.size[1]

    #đọc các pixel trong ảnh
    anh = ''
    for i in range(width):
        for j in range(height):
            #đọc giá trị từng điểm ảnh tại i, j
            R, G, B = img.getpixel((i, j))
            R, G, B = aes.dec_to_bin8(R), aes.dec_to_bin8(G), aes.dec_to_bin8(B)
            pix = str(R) + str(G) + str(B)
            pix = aes.bin_to_hex(pix)
            anh += pix
    anh = encryptCFB(anh, key)
    anh = aes.divide(anh, 2)
    i = 0
    for x in range(width):
        for y in range(height):
            R, G, B = int(anh[i], 16), int(anh[i+1], 16), int(anh[i+2], 16)
            i += 3
            binimg.putpixel((x, y), (R, G, B))
    binimg.show()


bin_img(img)


