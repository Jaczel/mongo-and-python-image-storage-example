#!/usr/bin/python

'''
Inserting a thumbnail into MongoDB
Larger images will need to use the GridFS library
'''

from PIL import Image
from pymongo import MongoClient
import datetime
import base64

thumbnail = Image.open('./static/thumbnail.png')

client = MongoClient('localhost', 27017)
# Replace this with whatever database you have on your system
db = client['angular-flask-muckaround']
user_collection = db['users']

user_collection.insert_one({
    "First Name": "Joseph",
    "Last Name": "Aczel",
    "Avatar": base64.b64encode(thumbnail.tobytes()),
    "Creation Date": datetime.datetime.now()
})
