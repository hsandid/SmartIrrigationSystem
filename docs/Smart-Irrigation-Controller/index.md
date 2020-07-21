---
layout: default
title: Smart Irrigation Controller
has_children: true
nav_order: 3
---

### Diagram - Smart Irrigation Controller

![SIC Diagram](../../assets/images/Diagram-SmartIrrigationController.png)

---

- The *Smart Irrigation Controller* is a modular hardware solution to control irrigation routines on agricultural fields. It has four different components :

### (1)  Raspberry-Pi Board

- We will be using the Raspberry-Pi 3 - Model B for our prototype.
- It will be fitted with a pre-configured micro-SD card containing *Raspbian* (recently renamed *Raspberry-Pi OS*), and all required packages & software.
- An *Apache* web server will be running constantly on the Raspberry-Pi. This web server will host the web interface, which allows farmers to control irrigation routines & receive information.
- A *Python* script will be running constantly on the Raspberry-Pi. This script will execute irrigation routines, periodically poll the flow meter for changes, and handle all traffic sent/received through the external wireless modules (i.e. LoRa and GSM transceivers).

### (2) Interface - Irrigation System

- The Raspberry-Pi board interfaces with different systems\utilities, to receive data and control irrigation routines.
- For our Prototype, we will assume that the Raspberry-Pi board only interfaces with a flow-meter and the main controller for a sprinkler irrigation system or furrow irrigation system

### (3) Interface  - Wireless Communication Modules

- The Raspberry-Pi board will be placed in the middle of agricultural fields, with little to no Wi-Fi\Bluetooth coverage. 
- We will be using LoRa and GSM transceivers to extend the effective range at which the Raspberry-Pi can operate and communicate with our cloud server.

### (4) Portable Power Solution

- The Raspberry-Pi must be powered constantly through its micro-USB port to function.
- To allow for portability, we will connect our Raspberry-Pi to a rechargeable battery, which in turn will be connected to a solar panel.