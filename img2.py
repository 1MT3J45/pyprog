import Image, ImageDraw
im = Image.open("lena.jpg")
# draw a grey cross over the image
draw = ImageDraw.ImageDraw(im)
draw.setink(128)
draw.line((0, 0), im.size)
draw.line((0, im.size[1]), (im.size[0], 0))
del draw
im.show()
