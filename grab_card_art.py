from PIL import Image
import requests
import urllib
import numpy as np
from io import BytesIO
import tensorflow as tf


def get_art(multiverseid):
    url = "https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid={}&type=card".format(multiverseid)
    print(url)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.load()
    img = scale_resize_image(img)
    return img

def make_square(img):
    cols,rows = img.size

    if rows>cols:
        pad = (rows-cols)/2
        img = img.crop((pad,0,cols,cols))
    else:
        pad = (cols-rows)/2
        img = img.crop((0,pad,rows,rows))
    return img


def scale_resize_image(image):
    image = tf.image.convert_image_dtype(image, tf.float32) 
    image = tf.image.resize(image, ( 320 , 265)) # Resizing the image dimention
    return (image)