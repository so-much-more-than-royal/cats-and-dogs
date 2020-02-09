import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import keras
import requests
import json
from keras.applications import models
import urllib
from PIL import Image
import numpy as np
from google.colab import drive, files
import os
import cv2

///////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////

drive.mount('/home')

///////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////

model = models.load_model('/home/My Drive/model.h5')

///////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////

def predict(image_url):
  image = Image.open(requests.get(image_url, stream=True).raw)
  image_array = np.array(image)
  input_for_model = np.reshape(cv2.resize(image_array, (200,200)), [1,200,200,3])/255
  prediction = model.predict(input_for_model)[0][0]
  return prediction
  
///////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////// 
 
              if update.message.photo:
                file_id = update.message.photo[-1].file_id
                image_url = bot.getFile(file_id).file_path

                prediction = predict(image_url)
               
                if prediction < 0.001:
                    answer = "Я думаю, что на фото кошка."
                elif prediction > 0.999:
                    answer = "Я думаю, что на фото собака."
                else:
                    answer = "Я не знаю, кто на фото."
                  
            else:
                answer = "Нет фото"
            update.message.reply_text(answer)
