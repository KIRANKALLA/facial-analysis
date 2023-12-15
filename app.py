import json
import cv2
import streamlit as st
from deepface import DeepFace
import numpy as np

image = st.file_uploader('Take your photo')
if image:
  st.image(image)
  image = np.array(image)
  information = DeepFace.analyze(image,actions = ['age'])
  age = information[0]['age']
  #emotion = information['dominant_emotion']
  #race = information['dominant_race']
  #gender = information['gender']
  st.write('Your age is  ' ,age)
  #st.write('You are from  ',race)
  #st.write('Your gender is ',gender)
  #st.write('You are feeling very  ',emotion)
