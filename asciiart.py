from PIL import Image
import numpy
import math

ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

openim = input("Image to load (include file extension): ")
im = Image.open(openim)

width = im.size[1];
height = im.size[0];
maxwidth = 60;
maxheight = 60;
ratio = min(maxwidth / width, maxheight / height);
im = im.resize((int(height*ratio), int(width*ratio)), Image.ANTIALIAS)

data = numpy.asarray(im)
brightness = numpy.zeros([im.size[1], im.size[0]])
ascii_matrix = numpy.chararray([im.size[1], im.size[0]], unicode=True)

for x in range(im.size[1] - 1):
    for y in range(im.size[0] - 1):
        avg = (int(data[x][y][0]) + int(data[x][y][1]) + int(data[x][y][2])) / 3
        brightness[x][y] = math.ceil(avg)
        index = int(math.floor(brightness[x][y] / 4))
        if index > 65:
            index = 65
        ascii_matrix[x][y] = ASCII[index]
        print(ascii_matrix[x][y], end='')
    print()