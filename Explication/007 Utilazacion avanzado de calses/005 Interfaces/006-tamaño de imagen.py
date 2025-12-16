from PIL import Image

imgen = Image.open("image.png")


tamanio = imgen.size
print(tamanio)


first_pixel = imgen.getpixel((0, 0))

print(first_pixel)
