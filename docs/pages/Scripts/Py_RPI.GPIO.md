---
title: "Python3 - RPI.GPIO Library"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: Py-RPI-GPIO-Library.html
folder: Scripts
---


## Initialization


- Importing the 'RPi.GPIO' library

```py
import RPi.GPIO
```
- Select a pin numbering system

```py
#BOARD numbering system
GPIO.setmode(GPIO.BOARD)

#BCM numbering system
GPIO.setmode(GPIO.BCM)
```
- Configure channel as an input:
```py
#With Pull-up resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#With Pull-down resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
```
- Configure channel as an output:
```py
GPIO.setup(channel, GPIO.OUT)
```
---

## I/O configuration


- (Input) Poll GPIO pins
```py
if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')
```
- (Input) Input detection using Wait_for_edge() function
```py
GPIO.wait_for_edge(channel, GPIO.RISING)
```
- (Output) Set GPIO pin as high/low
```py
#Set output as high
GPIO.output(<CHANNEL>, GPIO.HIGH)

#Set output as low
GPIO.output(<CHANNEL>, GPIO.LOW)
```
---

## Cleanup


To cleanup any used resources, you can call the following : 
```py
GPIO.cleanup()
```

## Source
- [Official RPI.GPIO Documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki)
