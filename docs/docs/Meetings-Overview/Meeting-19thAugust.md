---
layout: post
title:  "Week #11 (August 19th)"
parent: Meetings Overview
nav_order: 11
---

# Meeting #11 - August 29th

### Work Completed during this Week

- Selecting PCB components to order
   - List is available [here]()
- Redesigning the PCB board
   - There doesn't to be a common pattern amongst breakout board for the LoRa transceivers and GSM Module, so I based my design on the following components :
     - LoRa Transceiver : *MTXDOT-EU1-A00-1*
     - GSM Module : *NL-SW-GPRS*
   - Almost all modules and breakout boards found on the market for LoRa and GSM include some sort of direct antenna connector. I did not look into the RF side of things, especially when it comes to PCB traces.
   - Updated version of the PCB design can be found [here]()
- Final Deliverable - Design Document
   - I have started writing a design document summarizing my work on the Smart Irrigation Controller.
   - This design document follows the Standard IEEE requirement document outline, which I have added [here]() (*Credits : Dr. Mazen Saghir, EECE425 - Embedded Microprocessor Systems Design*) 
   - Topics I have started covering :
      - Performance and expected power usage of the Raspberry-Pi model we are using in our prototype (Raspberry-Pi 3 Model B).
      - Specify all open-source and licensed software we are using, and which we will package into a standalone image to use with our *Smart Irrigation Controller*.
      - PCB Interface we've designed for the *Smart Irrigation Controller*, with a mention of what CAD tool we've used, any additional Symbols & Footprints we had to design ourselves, and which specific or general modules our PCB targets.
      - Compatibility issues & region our *Smart Irrigation Controller* is targeted at.
      - Web Interface for the *Smart Irrigation Controller*.
      - Planned use of the Levantine Mobile Application to control the *Smart Irrigation Controller*.

### Formalities related to Internship

- "Letter from Employer" is required for me to validate my internship
- Expected Format :

![Letter-From-Employer](../../assets/images/Letter-From-Employer.PNG)

### (Unrelated Questions) Embedded Software

- IoT systems ?
- Networking devices ?
- Machine Learning ?
- 3d Applications & Virtual Reality ?