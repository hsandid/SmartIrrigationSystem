---
title: "Reducing the System's Power Usage"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: Lowering-The-System-Power-Consumption.html
folder: Powering-The-System
---


- The Raspberry-Pi does not offer a '*stand-by*' mode. We will need to manually manage the board's components and any running software to achieve the lowest power consumption when the Pi is idle or under use.

### Software running on the *Smart Irrigation Controller*

We will be using *'Lite'* OS on our Raspberry-Pi, with contains only the daemons & user processes necessary for the *Smart Irrigation Controller* to operate :

- Essential Raspbian daemons (like *CRON*).
- *Apache Web Server*, to have the Web Interface up-and-running. 

- Irrigation Control Script (Python-based) 
- *INCRON*, which is a similar program to *CRON* but instead of running commands based on time, it triggers commands based on file/directory events. We will use it in the *Smart Irrigation Controller* to modify *CRON* jobs according to user preferences on the Web interface.

### Handling Hardware Required by the *Smart Irrigation Controller*

The following components are required for the *Smart Irrigation Controller* to operate properly. These components will be turned on/off to conserver power, depending on the needs of the *Smart Irrigation Controller* :

- LoRa Transceiver OR GSM Module
- Any additional device connected to the GPIO interface for Irrigation control (i.e. flow meters, actuators...).

### Disabling Raspberry-Pi On-Board Components

Some of the components present on the Raspberry-Pi are not necessary to the functioning of the *Smart Irrigation Controller*, and as such it is preferable to disable them. Raspbian-OS allows us to disable most of these components through software :

- On-Board HDMI Port
- On-Board USB Ports 
- On-Board Wi-Fi Module
- On-Board Bluetooth Module
- On-Board CSI Camera Port
- On-Board DSI Display Port 
- On-Board 4-Poles Stereo Output and Composite Video Port 
- On-Board LEDs

### Source

- [HowToForge - What is Incron ?](https://www.howtoforge.com/tutorial/trigger-commands-on-file-or-directory-changes-with-incron/)