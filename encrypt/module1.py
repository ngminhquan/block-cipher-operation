import numpy as np
from PIL import Image
import aes
#img = Image.open('anhtest.jpg')
#img.show()
img = Image.open('anhtest.jpg')
key = '0f1571c947d9e8590cb7add6af7f6798'

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
    anh = aes.divide(anh, 2)
    i = 0
    for x in range(width):
        for y in range(height):
            R, G, B = int(anh[i]), int(anh[i+1]), int(anh[i+2])
            i += 3
            binimg.putpixel((x, y), (R, G, B))
    Image.show(anh)


    #newimg = np.array(binimg)
    #Image.show(newimg)

bin_img(img)


