---
title: "Raspberry-Pi 3 Model B"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: Raspberry-Pi-3-Model-B.html
folder: Raspberry-Pi-Model-Information
---


![Image of Rasp3 modelB](https://images-na.ssl-images-amazon.com/images/I/71EPckcD8ZL._AC_SL1244_.jpg)

- **Processor :** 

  - Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz (Quad-core processor).
  
  
  
- **Networking :**

  - Dual-band wireless LAN / 2.4GHz and 5GHz IEEE 802.11.b/g/n/ac Wireless LAN
  - Bluetooth 4.2/BLE (Bluetooth Low-Energy)
  - Ethernet port
  - Power-over-Ethernet support (Needs separate module)

  

- **RAM :** 

  - 1GB LPDDR2 SDRAM

  

- **GPIO Interface :** 

  - Extended 40-pin GPIO header
  - GPIO output pins can set to high (3.3V) or low (0V) \ GPIO input pins can be read as high (3.3V) or low (0V).
  - Internal pull-up or pull-down resistors are present on each pins. Pins GPIO2-GPIO3 have fixed pull-up resistors, but other pins can be configured in software.
  - Raspberry-Pi supports Pulse-Width modulation
    - Software Pulse-Width Modulation is available on all GPIO pins.
    - Hardware Pulse-Width Modulation is available on pins GPIO12, GPIO13, GPIO18, GPIO19.
  - Raspberry-Pi supports UART with the following pin configuration :
    - RX(GPIO15), TX (GPIO16) 
  - Raspberry-Pi supports SPI with the following pin configuration :
    - SPI0: MOSI (GPIO10); MISO (GPIO9); SCLK (GPIO11); CE0 (GPIO8), CE1 (GPIO7)
    - SPI1: MOSI (GPIO20); MISO (GPIO19); SCLK (GPIO21); CE0 (GPIO18); CE1 (GPIO17); CE2 (GPIO16)
- Raspberry-Pi supports I2C with the following pin configuration :
    - EEPROM Data: (GPIO0); EEPROM Clock (GPIO1); Data: (GPIO2); Clock (GPIO3)
  
  


![Raspberry-Pi 3 GPIO Interface](https://www.raspberrypi.org/documentation/usage/gpio/images/gpiozero-pinout.png)



- **Other Interfaces :**
    - 4x USB 2.0 ports

    - CSI camera port for connecting a Raspberry Pi camera

    - DSI display port for connecting a Raspberry Pi touchscreen display

    - 4-pole stereo output and composite video port

    - Micro SD port for loading your operating system and storing data.

    - 1x Full-size HDMI port

  

- **Required Power :** 

  - Typical PSU current capacity is 2.5A
  - Typical bare-board active current consumption is 400mA
  - Maximum total USB peripheral current draw is 1.2A
  - Recommended micro-USB connector : 5 V/2.5 A DC



- **Miscellaneous Information :**
  - The Raspberry-Pi 3 Model B will remain in production until January 2026.
  - Global compliance and safety certificates [here](https://www.raspberrypi.org/documentation/hardware/raspberrypi/conformity.md)
  - Operating temperature : 0-50°C
  - Raspberry-Pi 3 Model B mechanical drawing available [here](https://github.com/raspberrypi/documentation/raw/master/hardware/raspberrypi/mechanical/rpi_MECH_3bplus.pdf)
  - Raspberry-Pi 3 Model B schematic diagrams available [here](https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf)



## Resources

- [Raspberry-Pi 3 Model B, Official Page](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)