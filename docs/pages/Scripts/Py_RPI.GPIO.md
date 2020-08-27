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


- Importing the 'RPI.GPIO' library

```python
import RPi.GPIO
```
- Select a pin numbering system

```python
#BOARD numbering system
GPIO.setmode(GPIO.BOARD)

#BCM numbering system
GPIO.setmode(GPIO.BCM)
```

- Configure channel as an input:

```python
#With Pull-up resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#With Pull-down resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
```

- Configure channel as an output:

```python
GPIO.setup(channel, GPIO.OUT)
```

---

## I/O configuration


- Poll GPIO pins

```python
if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')
```

- Input detection using Wait_for_edge() function

```python
GPIO.wait_for_edge(channel, GPIO.RISING)
```

- Set GPIO pin as high/low

```python
#Set output as high
GPIO.output(<CHANNEL>, GPIO.HIGH)

#Set output as low
GPIO.output(<CHANNEL>, GPIO.LOW)
```
---

## Clean-up


To clean-up any used resources, you can call the following : 

```python
GPIO.cleanup()
```

## Source
- [Official RPI.GPIO Documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki)
