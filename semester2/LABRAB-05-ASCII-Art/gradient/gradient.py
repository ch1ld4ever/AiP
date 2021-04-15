from PIL import Image

img = Image.open("white.jpg")

width, height = img.size

kx = 256 / width 
ky = 256 / height 

for y in range(height, 0, -1 ):
    for x in range(y):
        clr = int(kx * x)
        r, g, b = clr , clr , clr
        img.putpixel((x , y - 1), (r + 25, g + 25, b + 112))
        img.putpixel((x//2 , y - 1), (r + 128, g + 0, b + 0))
        img.putpixel((x//4 , y - 1), (r + 0, g + 0 , b + 0))
img.show()

