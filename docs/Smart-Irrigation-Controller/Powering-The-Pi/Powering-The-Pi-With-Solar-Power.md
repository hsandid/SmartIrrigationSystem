---
layout: post
parent: Powering the Pi
title:  Powering the Pi with Solar Power
nav_order : 3
grand_parent : Smart Irrigation Controller
---


# Powering the Pi with Solar Power

- We'd like to develop a portable power solution using solar energy to power our *Smart Irrigation Controller*.
- We intend for the *Smart Irrigation Controller* to be connected to a rechargeable battery, which would supply it with 5V. The rechargeable battery will be in turn connected to a portable solar panel, which would provide it with enough electrical energy to run our *Smart Irrigation Controller*.
- **Important** : The Pi supports a 5V input power. If out battery supplies more than 5V input power, we might have to use additional circuitry (i.e. Voltage Divider Circuit, DC/DC Power Converter, Linear Voltage Regulator) to reduce its input power to the Pi.

![Solar Energy Solution Diagram](../../../assets/images/Diagram-Solar-Energy.PNG)

# Selecting components

- **Battery** : We require a battery which can output the recommended 5V @ 2A. There are many battery models available and we can find a suitable model later on.
- **Solar Panel** : We need a solar panel able to support a battery outputting 5V @ 2A. A close match would be this [model](https://www.adafruit.com/product/2747) from Adafruit.

- **Interface with the Raspberry-Pi** :  To power the Pi, we can connect our battery to either the Micro-USB port , or through specific pins of its GPIO interface.