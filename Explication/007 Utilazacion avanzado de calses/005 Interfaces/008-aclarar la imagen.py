from PIL import Image

imgen = Image.open("image.png")

anchura,altura = imgen.size

for x in range(0,anchura):
    for y in range(0,altura):
        pixel = imgen.getpixel((x,y))
        rojo = pixel[0]
        verde = pixel[1]
        azul = pixel[2]

        rojo += 20
        verde += 20
        azul +=20
        pixel = (rojo,verde,azul)

imgen.save("modificado.jpg")
