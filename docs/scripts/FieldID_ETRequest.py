#Import the RPi.GPIO library
import RPi.GPIO as GPIO

#Import the time library
import time

#Import the requests library 
import requests 

#Import the JSON library
import json

#Initializing GPIO ports
#GPIO Pin 2 is assigned as output (Red LED on circuit)
#GPIO Pin 3 is assigned as output (Green LED on circuit)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)

  
#Defining the API-endpoint  
API_ENDPOINT = "<BACKEND_URL>/tiff/coordinates_to_et/<FIELD_ID>"

#Defining Headers
headers = {'Content-Type' : 'application/json'}
  
#Sending Get request and saving response as response object 
r = requests.get(url = API_ENDPOINT, headers=headers) 
  
#Extracting text response 
textresponse = r.json()

#Check if the response contains a valid ET value
#If the ET value is valid, flash the Green LED according to the ET value
#If the ET value is invalid, flash the Red LED once

if textresponse.get('et_value') is None:
    print("No ET value for this field!")
    GPIO.output(2,GPIO.HIGH)
    time.sleep(3)

else :
    Et_Value = float(textresponse.get('et_value'))
    Et_Value = int(Et_Value)
    print(Et_Value)

    for x in range(5):
        GPIO.output(3,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(3,GPIO.LOW)
        time.sleep(0.5)