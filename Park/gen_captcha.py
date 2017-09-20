# coding: utf-8

import os
import random
from PIL import Image, ImageDraw, ImageFont
# import ImageDraw
# import ImageFont
from tempfile import NamedTemporaryFile

PWD = os.getcwd()
SEP = os.path.sep
FONT_FILE = SEP.join([PWD, "VeraMono.ttf"])
FONT_SIZE = 35
POOL = "1234567890ABCDEFGHIJKLNMOPQRSTUVWXYZ"

LENGTH = 6
WIDTH = 135
HEIGHT = 50

R = random.randint(0,256)
G = random.randint(0,256)
B = random.randint(0,256)

def generate_captcha(PATH=PWD):
    """
    Parameters:
        PATH – path to where captha image will be stored

    Description:
        using PIL, generate captcha image and its value and return them.
        generated captha image is not encrypted,
        this module simply generate a image for the random character value
        if you want to encrypting captcha library,
        you should find other library like python-recaptcha or something.
    """
    """Modified by JiSoo
        1. Characters and Colors are generated randomly
        2. image file name and value are equal
        3. Captcha file dir is changed(captcha_image)"""
    with NamedTemporaryFile(suffix='.jpg', dir=PATH,delete=False) as fp:
        im = Image.new("RGB", (WIDTH, HEIGHT), (R, G, B))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(FONT_FILE, FONT_SIZE, encoding='unic')

        value = "".join(random.sample(POOL, LENGTH))
        #value = "354DD5"
        draw.text((5, 1), value, font=font,fill=(256-R,256-G,256-B))

        #im.save(fp.name)
        im.save("./captcha_image/"+value+".jpg")
        im.show()
        fp.close()
        os.remove(fp.name)#임시파일 생성된 것을 삭제해줌
        return im, value

if __name__ == '__main__':
    print(generate_captcha())