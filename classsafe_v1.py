# -*- coding: utf-8 -*-
"""ClassSafe V1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xYn3oRPpT5pgJ55ofCbHSGm2Qxte7IIY
"""

!pip install pyrebase
import pyrebase
!pip install deepface
import deepface
import requests
from deepface import DeepFace
import pandas as pd
from datetime import datetime

config = {
    "apiKey": "jLru8dYry0Cr6XwnQeQ4nUe7YDKm8qwk96HvFvbB",
    "authDomain": "classsafe-5ed5e.firebaseapp.com",
    "databaseURL": "https://classsafe-5ed5e-default-rtdb.firebaseio.com",
    "projectId": "classsafe-5ed5e",
    "storageBucket": "classsafe-5ed5e.appspot.com",
    "messagingSenderId": "102510651293",
    "appId": "1:102510651293:web:9ef47472b6314a0ea5b174",
    "serviceAccount": "/content/classsafe-5ed5e-firebase-adminsdk-byfil-0ce5d0795d.json"
}

firebase = pyrebase.initialize_app(config)
database=firebase.database()
database.child('lockstatus').set('locked')
database.child('tempLoginVal').set(2)
#


#
id=database.child("picid").get()
intId=id.val()
#

#
storage=firebase.storage()
storage.child("downloaded.png").download("downloaded.png")
#

allFiles = storage.list_files()
for file in allFiles:
  file.download_to_filename("/content/refphotos/" + file.name)

now = datetime.now()
current_time = now.strftime("10:%M:%S")
currentstudent = 'Akhil Ramidi'

df = DeepFace.find(img_path = "downloaded.png", db_path = "/content/refphotos")
print(df.head())

if(len(df.identity) > 0):
  database.child('lockstatus').set('unlocked')
  database.child('tempLoginVal').set(1)
  database.child('time').set(current_time)
  database.child('studentname').set(currentstudent)

#After 10 seconds of the door being unlocked
database.child('lockstatus').set('locked')
database.child('tempLoginVal').set(2)
database.child('time').set('null')
database.child('name').set('null')