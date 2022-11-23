
from PIL import Image
img = Image.open('anhtest.jpg')
#img.show()
#new_img = img.convert('L')
n = img.getpixel((4,5))
#new_img.show()
#print(n)

def add_uint8(a, b, c):
    av = (a + b + c)/3
    if av >255:
        av = av - 255
    return av
print(add_uint8(100, 100, 200))
#print(add_uint8(1,5))