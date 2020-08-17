---
layout: post
title:  "Week #11 (August 19th)"
parent: Meetings Overview
nav_order: 11
---

# Meeting #11 - August 29th

### Work Completed during this Week

- Selecting PCB components
   - LoRa Transceiver (UART)
      - Preferably we'd like our Transceiver to be a a separate module or on a breakout board. If these are not available, we can go with a Pi-Hat
      - The LoRaWAN gateways can be either bough as a separate module, or we can buy a Raspberry-Pi alongside the LoRaWAN gateway module.
   - LoRaWAN Gateway Module
   - **IMPORTANT** : Both the LoRa Transceiver and LoRaWAN Gateway module should support a common channel plan, which should be either EU433 (433-435Mhz) or EU863-870 (862-870MHz).
   - GPS Module (UART)
   - Antenna for LoRa Transceiver ?
   - Antenna for LoRa Gateway ?
   - Antenna for GPS Module ?
   - Connector Pin Female 40-Pins
- Redesigning the PCB board
   - As requested I've redesigned the PCB board to work with common breakout boards for LoRa Transceivers and GSM Modules, while keeping the remaining GPIO ports available for use.
   - GPIO Pins used :
   - GPIO Pins free :
- Raspberry-Pi automation
   - Script : Disable all unnecessary components of the Pi to save power
   - Script : Install Apache Web Server & Setup Smart Irrigation Web Interface