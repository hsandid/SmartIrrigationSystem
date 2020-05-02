#Import the RPi.GPIO library
import RPi.GPIO as GPIO
#Import the time library
import time
#Import the requests library 
import requests 
#Import the JSON library
import json

#Initializing GPIO ports
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)

  
#Defining the API-endpoint  
API_ENDPOINT = "https://promising-keep-261206.appspot.com/tiff/coordinates_to_et/0D2o42T4238dVssuBEdg"

#Defining Headers
headers = {'Content-Type' : 'application/json'}
  
#Sending Get request and saving response as response object 
r = requests.get(url = API_ENDPOINT, headers=headers) 
  
#Extracting text response 
textresponse = r.json()

#Check if the response contains a valid ET value and act accordingly
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
    
