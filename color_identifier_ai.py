from calendar import EPOCH
from re import I
from string import capwords
from tracemalloc import start
from turtle import color
import tensorflow as tf
import numpy as np
from grab_card_art import get_art
from db_connect import query_local
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential

import matplotlib.pyplot as plt
import seaborn as sns

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

from sklearn.metrics import classification_report,confusion_matrix

import tensorflow as tf

import cv2
import os

import numpy as np

import time


def collect_data():
    test = True
    color_group_query = "select distinct colors from cards"
    color_group = query_local(color_group_query)
    iter = 0
    color_number_index = []
    for diff_color in color_group:
        new_index = {
            'id': iter,
            'color': diff_color[0] or 'colorless',
        }
        color_number_index.append(new_index)
        iter += 1
    start_time = time.time()
    card_query = "select name,multiverseId,colors from cards where multiverseId is not null order by multiverseId asc limit 10"
    if test:
        card_query = "select card_name.name, card_name.multiverseId, card_color.colors from cards card_color join cards card_name on card_color.id = card_name.id where card_color.multiverseId is not null group by card_color.colors"
    card_array = query_local(card_query)
    card_dict_array = []
    for card in card_array:
        for colors in color_number_index:
            if card[2] is None:
                color = 'colorless'
            else:
                color = card[2]
            if color == colors['color']:
                color_index = colors['id']
        dict_element = {
            "name": card[0],
            "multiverseid": card[1],
            "color": color_index
        }
        card_dict_array.append(dict_element)
    print(card_dict_array)
    vector_array = []
    colors_array = []
    for dict in card_dict_array:
        vector_array.append(get_art(dict["multiverseid"]))
        colors_array.append(dict["color"])
    end_api_time = time.time()
    api_time_interval = end_api_time - start_time
    print("Request Time: {} seconds".format(api_time_interval))
    drive_ai(vector_array,colors_array,color_number_index)


def drive_ai(cards,colors,color_number_index):

    # image_size = (265, 320)
    batch_size = 32


    plt.figure(figsize=(10,10))
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(cards[i])
        for color in color_number_index:
            if int(colors[i]) == color['id']:
                name = color['color']
        plt.title(name)
    plt.show()
    
    model = Sequential()

    model.compile(optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])




    model.fit(cards, epochs=500)

    gurrak = get_art(519225)
    answer = model.predict([gurrak])
    print("Answer: ",answer)


collect_data()
