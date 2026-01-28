from PIL import Image

imgen = Image.open("image.png")

anchura,altura = imgen.size

for x in range(0,anchura):
    for y in range(0,altura):
        first_pixel = imgen.getpixel((x,y))
        print(first_pixel)
