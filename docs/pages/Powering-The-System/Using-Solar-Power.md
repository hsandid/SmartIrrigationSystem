---
title: "Using Solar Power"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: Using-Solar-Power.html
folder: Powering-The-System
---


- We'd like to develop a portable power solution using solar energy to power our *Smart Irrigation Controller*.
- We intend for the *Smart Irrigation Controller* to be connected to a rechargeable battery, which would supply it with 5V. The rechargeable battery will be in turn connected to a portable solar panel, which would provide it with enough electrical energy to run our *Smart Irrigation Controller*.
- **Important** : The Pi supports a 5V@2A input power. If our battery supplies more than 5V input voltage, we might have to use additional circuitry (i.e. Voltage Divider Circuit, DC/DC Power Converter, Linear Voltage Regulator) to reduce its input power to the Pi. Also, we might want to include a Current Regulator circuit to control the input current based on the boards' needs.

![Solar Energy Solution Diagram](../../images/Diagram-Solar-Energy.PNG)

# Selecting components

- **Solar Panel** : We need a solar panel able to support a battery outputting 5V @ 2A. A close match would be this [model](https://www.adafruit.com/product/2747) from Adafruit.
- **Battery** : We'd like to provide an input power of 5V @ 2A to the Raspberry-Pi. There are many battery models available, but we'd likely have to add some voltage/current limiting circuits in-between the battery and the Raspberry-Pi.
- **Interface with the Raspberry-Pi** :  To power the Pi, we can connect our battery to either the Micro-USB port , or through specific pins of its GPIO interface. We need to see what interfaces is more suitable to our implementation.