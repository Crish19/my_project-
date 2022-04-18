
import re
import os
from this import s 
import requests
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

#this code works in extrating the geolocation of a picture but I can not 
# convert DMS to DD in order for google maps to read and give me a location on a map. 

api_key = ''

# def get_latlon_conversion (dms,ref):
#     degrees = dms [0][0] / dms [0][1]
#     minutes = dms [1][0] / dms [1][1] / 60.0
#     seconds = dms [2][0]/ dms [2][1] / 3600.0 

#     if ref in ['S','W']:
#         degrees = -degrees
#         minutes = -minutes
#         seconds = -seconds 

#     return round (degrees + minutes + seconds, 5)



def get_exif (filename):
    image = Image.open (filename)
    image.verify() 
    return image._getexif()

def get_coordinates (exif):
    lat = exif[34853][2]
    latRef = exif[34853][1]
    lon = exif[34853][4]
    lonRef = exif[34853][3]
    
    
    # lat = get_latlon_conversion (lat, latRef)
    # lon = get_latlon_conversion (lon, lonRef) 

    print (lat, lon)
    print (lat,latRef, lon, lonRef)

def get_geo ( latlon , key_file):
    r = requests.get ('https://maps.googleapis.com/maps/api/geocode/json?latlon='+ latlon + '&key='+ api_key)

exif = get_exif ('sol.jpg')
coordinates = get_coordinates (exif)

get_geo (str(coordinates)[1:-1],'sol.jpg')
