---
layout: post
title:  "Raspberry-Pi 3 - Model B"
parent: Raspberry-Pi Hardware
nav_order: 1
---

# Raspberry-Pi 3 - Model B Specifications

![Image of Rasp3 modelB](https://www.raspberrypi.org/homepage-9df4b/static/3198932bc370441e554eb72e9713e12b/052d8/67d8fcc5b2796665a45f61a2e8a5bb7f10cdd3f5_raspberry-pi-3-1-1619x1080.jpg)

- **Processor :** 

  - Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz (Quad-core processor).
  
- **More about Processors :**

  - 32-bit processor vs 64-bit processor :

    - 32-bit processors support up to <img src="https://render.githubusercontent.com/render/math?math=2^{32} "> bytes of memory, or around <img src="https://render.githubusercontent.com/render/math?math=4">GB of memory.
    - 64-bit processors support up to <img src="https://render.githubusercontent.com/render/math?math=2^{64} "> bytes of memory, or around  <img src="https://render.githubusercontent.com/render/math?math=17*10^{9}"> GB of memory.

  - Raspberry-Pi OS (*a.k.a.* Raspbian OS) only has a 32-bit version. It is designed to run on all Raspberry-Pi boards, including earlier versions which had a 32-bit processors only.

    - 64-bit processors support both 32-bit and 64-bit OSes.
    - 32-bit processors support only 32-bit OSes.

  - 32-bit support is being slowly dropped. We may have to migrate our system to a 64-bit system, and 64-bit software.

    

- **Networking :**

  - Dual-band wireless LAN / 2.4GHz and 5GHz IEEE 802.11.b/g/n/ac Wireless LAN
  - Bluetooth 4.2/BLE (Bluetooth Low-Energy)
  - Ethernet port
  - Power-over-Ethernet support (Needs separate module)

- **More about Networking :**

  - Wi-Fi Standards Evolution
    - 802.11b - *1999*
      - 2.4 GHz frequency
      - Bandwidth rate of 11 Mbps
      - Range of 45 meters
    - 802.11a - *1999*
      - 5 GHz frequency
      - Bandwidth rate of 54 Mbps
      - Range of 30 meters
    - 802.11g - *2003*
      - 2.4 GHz frequency
      - Bandwidth rate of 54 Mbps
      - Range of 45 meters
    - 802.11n - *2009*
      - 2.4/5 GHz frequency
      - Bandwidth rate of 300 Mbps
      - Range of 50 meters
    - 802.11ac - *2014*
      - 5 GHz frequency
      - Bandwidth rate of 433 Mbps and up
      - Range of 50 meters

  

- **RAM :** 

  - 1GB LPDDR2 SDRAM

  

- **Interface :** 

  - Extended 40-pin GPIO header

    - GPIO output pins can set to high (3.3V) or low (0V)
    - GPIO input pins can be read as high (3.3V) or low (0V).
      - Internal pull-up or pull-down resistors are present on each pins. Pins GPIO2-GPIO3 have fixed pull-up resistors, but other pins can be configured in software.
    - Raspberry-Pi supports Pulse-Width modulation
      - Pulse width modulated signal frequency and duty-cycle can be modified.
      - Software Pulse-Width Modulation is available on all GPIO pins.
      - Hardware Pulse-Width Modulation is available on pins GPIO12, GPIO13, GPIO18, GPIO19.
    - Raspberry-Pi supports SPI over it's UART interface
      - SPI0: MOSI (GPIO10); MISO (GPIO9); SCLK (GPIO11); CE0 (GPIO8), CE1 (GPIO7)
      - SPI1: MOSI (GPIO20); MISO (GPIO19); SCLK (GPIO21); CE0 (GPIO18); CE1 (GPIO17); CE2 (GPIO16)
    - Raspberry-Pi supports I2C over it's UART interface
      - EEPROM Data: (GPIO0); EEPROM Clock (GPIO1); Data: (GPIO2); Clock (GPIO3)

    

    ![Image of Rasp3 modelb](https://www.raspberrypi.org/documentation/usage/gpio/images/gpiozero-pinout.png)

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
  - Global compliance and safety certificates [here]((https://www.raspberrypi.org/documentation/hardware/raspberrypi/conformity.md)
  - Operating temperature : 0-50°C
  - Raspberry-Pi 3 Model B mechanical drawing available [here](https://github.com/raspberrypi/documentation/raw/master/hardware/raspberrypi/mechanical/rpi_MECH_3bplus.pdf)
  - Raspberry-Pi 3 Model B schematic diagrams available [here](https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf)



## Resources

- [Raspberry-Pi 3 Model B, Official Page](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
