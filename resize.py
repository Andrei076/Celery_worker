from PIL import Image
import os

size = 512
basewidth = 512


def resizer(infile):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        new_img = im.resize((basewidth, size), Image.ANTIALIAS)
        new_img.mode = 'RGB'
        new_img.save(file + "_resized.jpg", "JPEG")


if __name__ == '__main__':
    resizer('uploads/sign_stop_PNG25636.png')
