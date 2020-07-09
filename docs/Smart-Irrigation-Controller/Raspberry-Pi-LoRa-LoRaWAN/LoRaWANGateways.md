---
layout: post
parent: LoRa & LoRaWAN Technology
title:  LoRaWAN Gateways
grand_parent : Smart Irrigation Controller
---
# LoRaWAN Gateways

- Do we need more than one channel for the prototype ?
- Most models mentioned here are carrier grade and very expensive (1k+$). Raspberry-Pi with a module seems to be the most low-cost soluton (under 200$).
- Open-source code has been made available by Semtech, which produces the LoRaWAN gateway chips present in all products here. Code is available [here](https://github.com/Lora-net/lora_gateway). Whatever device we choose, I can use this code and other Raspberry-Pi libraries to configure the LoRaWAN gateway.

### LoRaWAN Gateways (using a Raspberry-Pi & LoRaWAN gateway module)

- [Sparkfun.com, LoRa Raspberry-Pi Gateway with Enclosure](https://www.sparkfun.com/products/15336) (Link proposed in mail)
- Fully assembled gateway containing a Raspberry-Pi board, 915Mhz compatible antenna, GPS shield and all extra components required to run both the board and the LoRaWAN gateway module.
    - LoRaWAN Concentrator Engine : Semtech SX1301 - 8 channels
    - **May not fit our needs :** "Designed for 915MHz US/Australia LoRA ISM band". While the on-board LoRaWAN chip supports 868MHz, the antenna shipped with the enclosure supports 915MHz only (US standard). Maybe we can use our own custom settings to run on 868MHz, as the Semtech chip supports it ?
    - Price : 199.95 $


- Lite Gateway Platform on [IMST](https://shop.imst.de/wireless-modules/lora-products/36/lite-gateway-demonstration-platform-for-lora-technology)
  - Pre-configured Raspberry-Pi board + iC880A-SPI chip. See iC880A-SP chip details [here](https://shop.imst.de/wireless-modules/lora-products/8/ic880a-spi-lorawan-concentrator-868-mhz)
  - Price : Around 230$

- [SparkFun LoRa Gateway - 1-Channel (ESP32)](https://www.sparkfun.com/products/15006) + Raspberry-Pi
  - One LoRa channel support
  - Supports Wi-Fi and Bluetooth
  - Supports 868/915MHz LoRa frequencies
  - **May not fit our needs** : Designed to be connected with an Arduino board originally. I can still refactor parts of the libraries for it to work on the Raspberry-Pi
  - Price : 34.95$ (Sparkfun gateway) + Raspberry-Pi (100$)

- Building our own low-cost gateway
  - Main parts required
    - Raspberry-Pi board
    - iC880A-SPI concentrator board
    - RPi to iC880a interface
  - Guide available at [https://github.com/ttn-zh/ic880a-gateway/wiki]()

### LoRaWAN Gateways (Carrier-Grade)

- Laird
  - [Laird RG1xx Series](https://eu.mouser.com/new/laird-connectivity/laird-sentrius-rg1-lora-gateway/)
    - Up-to 8 LoRa channels support depending on the model
    - Different models supporting 868/915MHz LoRa frequencies
    - Different models supporting Wi-Fi and Bluetooth
    - Price : No specified price
- Kerlink
  - [Kerlink iBTS](http://www.kerlink.com/en/products/lora-iot-station-2/wirnet-ibts)
    - Up-to 8 channels support
    - Supports Wi-Fi and Bluetooth
    - Supports 868/915MHz LoRa frequencies
    - Price : No specified price
- Lorix
  - [LORIX One](http://lorixone.io)
    - Up-to 8 channels support
    - Supports Wi-Fi and Bluetooth
    - Supports 868/915MHz LoRa frequencies
    - Price : Around 500$
- AAEON
  - [Aaeon UP](http://industrialgateways.eu/docs/)
    - Up-to 8 channels support
    - Supports Wi-Fi and Bluetooth
    - Supports 868/915MHz LoRa frequencies
    - Price : Around 550$
- Cisco
  - [Cisco LoRaWAN Gateway](https://www.cisco.com/c/en/us/products/routers/wireless-gateway-lorawan/index.html)
    - Up-to16 channels support
    - Supports Wi-Fi and Bluetooth
    - Supports 868/915MHz LoRa frequencies
    - Price : 550$
- Gemtek
  - All Gemtek models available [here](https://www.gemteks.com/en/products/lora-iot/gateway)
    - Up-to 8 LoRa channels support depending on the model
    - Different models supporting 868/915MHz LoRa frequencies
    - Different models supporting Wi-Fi and Bluetooth
    - Price : No specified price
- Tekletic
  - All Tektelic models available [here](https://tektelic.com/iot/lorawan-gateways/)
    - Up-to 8 LoRa channels support depending on the model
    - Different models supporting 868/915MHz LoRa frequencies
    - Different models supporting Wi-Fi and Bluetooth
    - Price : No specified price
- Ursalink
  - [UG87 Outdoor Gateway](https://www.ursalink.com/en/ug87-lorawan-gateway/)
    - Up-to 8 channels support
    - Supports Wi-Fi and Bluetooth
    - Supports 868/915MHz LoRa frequencies
    - Price :No specified price



Source : [The Things Network - Commercially Available LoRaWAN Gateways ](https://www.thethingsnetwork.org/docs/gateways/start/list.html)