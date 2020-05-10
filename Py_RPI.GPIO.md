# Python3 - RPI.GPIO library
## Initialization
- Importing the 'RPi.GPIO' library

```python3 
import RPi.GPIO
```
- Select a pin numbering system

```python3 
#BOARD numbering system
GPIO.setmode(GPIO.BOARD)

#BCM numbering system
GPIO.setmode(GPIO.BCM)
```
- Configure channel as an input:
```python3 
#With Pull-up resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#With Pull-down resistor
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
```
- Configure channel as an output:
```python3 
GPIO.setup(channel, GPIO.OUT)
```
## I/O configuration
- (Input) Poll GPIO pins
```python3 
if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')
```
- (Input) Input detection using Wait_for_edge() function
```python3 
GPIO.wait_for_edge(channel, GPIO.RISING)
```
- (Output) Set GPIO pin as high/low
```python3 
#Set output as high
GPIO.output(<CHANNEL>, GPIO.HIGH)

#Set output as low
GPIO.output(<CHANNEL>, GPIO.LOW)
```
## PWM Function
More can be read about PWM configuration of GPIO pins here : https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
## Cleanup
To cleanup any used resources, you can call the following : 
```python3 
GPIO.cleanup()
```
## Source
- https://sourceforge.net/p/raspberry-gpio-python/wiki
