---
title: "Pi-Hat Official Specifications"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: Pi-Hat-Specifications.html
folder: Raspberry-Pi-Model-Information
---

# Official Pi-Hat Specifications

- Most Raspberry-Pi boards (Raspberry-Pi Model B+ and onwards) have been designed to support add-on boards, or 'HATs' (Hardware Attached on Top).



### HAT General Requirements

1. The HAT must have a full-size 40W GPIO connector, which spaces it at least 8mm from the Pi. It should also be taken into consideration when designing a HAT that the Raspberry-Pi 3 Model B+ has a 4-pin PoE (i.e. Power-Over-Ethernet) header near the top-right corner mounting hole. It should also not connect with the "RUN" or "PEN" header pins on the Raspberry-Pi.
2. 40W header on compatible Raspberry-Pi boards have 2 special pins (ID_SC and ID_SD) that are reserved for attachment to an ID EEPROM, which includes vendor information, GPIO map, and valid device tree information, that allows the Pi to set-up the required software for the HAT at boot time.
3. If our HAT offers Back-Powering through the 5V GPIO header pins, an ideal diode must be added for safety, in case the Pi 5V supply is also connected. The HAT should also be able to supply of 1.3A continuously to the Pi board, with 2A being the recommended value.
4. On older firmware, the GPIO pins #6, #14 and #16 might be accidentally driven at boot time. We should ensure that the HAT protects itself if this was to occur. 
5. The HAT design must take into consideration the existence of display/camera flex. It can still be considered a HAT even if the design cut-out does not allow for a display/camera flex, but it is not recommended.

- The Raspberry-Pi HAT Board Mechanical Specifications can be found [here](https://github.com/raspberrypi/hats/blob/master/hat-board-mechanical.pdf).



### Design Guide

- The design guide for Pi-HAT boards can be found [here](https://github.com/raspberrypi/hats/blob/master/designguide.md).



### Flashing the ID EEPROM

- ID EEPROM data format spec. sheet can be found [here](https://github.com/raspberrypi/hats/blob/master/eeprom-format.md).
- Tools and Documentation on how to flash ID EEPROMs is available [here](https://github.com/raspberrypi/hats/blob/master/eepromutils).



### Source

- [Raspberry-Pi, Github - Pi-HATs documentation](https://github.com/raspberrypi/hats)

