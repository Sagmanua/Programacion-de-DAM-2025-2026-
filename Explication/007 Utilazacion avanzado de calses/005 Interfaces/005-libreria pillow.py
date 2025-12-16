from PIL import Image

imgen = Image.open("image.png")

imgen = imgen.convert("RGB")

first_pixel = imgen.getpixel((0, 0))

print(first_pixel)
