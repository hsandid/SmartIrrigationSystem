---
title: "Presentation #1 - August 26th"
keywords: 
last_updated: 
tags: 
sidebar: meetings_sidebar
permalink: Presentation-26thAugust.html
folder: presentations
---

- Version : v01
- Presentation Topic : Overview of the Smart Irrigation System
- Number of Slides : 6 Slides
- Outline :
  - Slide #1 : Introductory Slide
    - Google AI Impact Challenge - Team Levantine
    - Smart Irrigation System
    - Fatima Abu Salem -  Hadi Jaafar - Mazen Saghir - Samer Kharroubi
    - `Diagram` : AUB Logo
  - Slide #2 : General Block Diagram of the Smart Irrigation System
    - CENTER : Smart Irrigation Controller
    - LEFT : Solar Power System
    - RIGHT : Back-End System
    - TOP : Irrigation System
    - `Diagram` : Overview of smart irrigation system
  - Slide #3 : Irrigation Controller + PCB Design and modules + Connecting to Irrigation Systems
    - Raspberry-Pi + PCB with additional modules
    - LoRa Support
    - GSM Support (2G/3G/4G)
    - Straightforward interface to connect with Irrigation Systems
    - `Diagram` : Raspberry-Pi, PCB with Modules
  - Slide #4 : Back-End API Calls and Analytics  & Connecting with the Back-End (LoRaWAN OR GSM)
    - The back-end system send data (i.e. ET Value) which is used to setup the irrigation routines, it also receives data related to the local irrigation routines
    - Large distance (5KM+) <-> Wi-Fi and Bluetooth cannot be used in this situation
    - Option #1 : LoRaWAN
    - Option #2 : GSM
    - `Diagram` : Smart Irrigation Controller distance with Back-End, Using LoRaWAN network, Using GSM Network
  - Slide #5 : Powering the *Smart Irrigation Controller* & Solar Panel with Battery
    - Issues deploying with access to power grid
    - Using a portable solar panel and battery in our design to power the *Smart Irrigation Controller*
    - Low-Power usage of the system & standby mode of PCB modules & autonomous functioning with status tracking
    - `Diagram` : Smart Irrigation Controller with Solar Power System
  - Slide #6 : Mobile Application & Web Interface
    - Mobile Application and Web Interface can be used to communicate with the *Smart Irrigation System*
    - We can receive field data and logs from the back-end, or set preferences for the Irrigation routine of the *Smart Irrigation Controller*.
    - `Diagram` : Smart Irrigation Controller and Back-End, with Phone and Web Interface displayed.



- Questions :
  - Terminology :  I am leaving the term *Smart Irrigation Controller* to describe only the Raspberry-Pi, and our custom PCB with additional modules. I am currently using the term *Smart Irrigation System* to describe the system as a whole, including back-end, solar-power system, and the *Smart Irrigation Controller*. Any issues with this terminology ?
  - Preface Slide : I have added an 'introduction' slide with the name of people on the tea. Should we keep it or do you want me to remove it for this presentation to make it more straightforward ?