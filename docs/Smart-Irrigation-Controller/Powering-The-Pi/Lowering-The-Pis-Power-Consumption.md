---
layout: post
parent: Powering the Pi
title:  Lowering the Pi's Power Consumption
nav_order : 2
grand_parent : Smart Irrigation Controller
---


# Reducing the Pi's Power Consumption

- The Raspberry-Pi does not offer a  '*stand-by*' mode. We will need to manage the board's components and any running software to achieve the lowest power consumption when the Pi is idle or under use.
- To lower the power consumption of the *Smart Irrigation Controller*, it is recommended to disable any unused interfaces on the Pi board, and limit the amount of daemons (i.e. background processes) or user processes running under Raspbian on the Pi system.

# Hardware

The following components are essential for the *Smart Irrigation Controller* to operate properly, however they will be turned off when not needed to conserve power :

- LoRa Transceiver OR GSM Module, any additional device connected to the GPIO interface for Irrigation control (i.e. flow meters...).

The following hardware components of the Raspberry-Pi are not required for the *Smart Irrigation Controller*, and will be disabled through software to conserve power :

- HDMI Port - USB Ports - Wi-Fi device - Bluetooth Device - CSI camera port - DSI display port - 4-pole stereo output and composite video port - On-board LEDs

# Software

We will be using Raspbian Lite on our Raspberry-Pi, with only the required daemons & user processes for the *Smart Irrigation Controller* to operate. Software running at all times includes :

- Raspbian OS daemons (most notably cron) - *Apache* Web Server running the Web Interface 

We'd also require the following processes to run periodically for the *Smart Irrigation Controller* to operate properly, they will be started by the *Cron* service and killed when not needed to conserve power :

- Irrigation Control Script (Python-based) - Incron**

***What is Incron ?* : Incron is a similar program to Cron, but instead of running commands based on time, it triggers commands based on file/directory events. We will use it in the *Smart Irrigation Controller* to modify *Cron* jobs according to user preferences on the Web interface.

# Source

- [HowToForge - What is Incron ?](https://www.howtoforge.com/tutorial/trigger-commands-on-file-or-directory-changes-with-incron/)