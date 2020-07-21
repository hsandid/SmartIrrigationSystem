---
layout: post
parent: LoRa & LoRaWAN
title:  LoRa Transceivers
grand_parent : Smart Irrigation Controller
---
# Selecting our LoRa Transceiver

- To allow our Raspberry-Pi board to receive\transmit data in a LoRaWAN network, we must equip it with a LoRa transceiver
- **IMPORTANT :** Our transceiver should operate on the ISM band  EU433\EU868, as it is not legal to operate on other LoRaWAN ISM bands in Lebanon (such as US915).

---



### **Type-1, Pi-Hat LoRa Transceivers** :

- Pi-Hats modules are designed to be compatible with the GPIO interface of the Raspberry-Pi.
- **IMPORTANT** : How many pins does each Pi-Hat model require ? If the Pi-Hat uses too much pins, we might not be able to connect the Raspberry-Pi to other components (i.e. flow meters, GSM modules...).

| Manufacturer  | Operating Frequency | Price | Store Link |
| ------- |  -------- |  ----- | ----- |
| Pi Supply | 868MHz & 915MHz versions available | 150 USD | [Link](https://uk.pi-supply.com/products/iot-lora-node-phat-for-raspberry-pi?_pos=41&_sid=30d832a4c&_ss=r)|
| IoT Store | 433MHz & 915MHz versions available | 60 USD | [Link](https://www.iot-store.com.au/products/lora-and-gps-hat-for-raspberry-pi-long-range-transceiver) |
| Waveshare  | 915MHz version available | 35 USD | [Link](https://www.amazon.com/SX1262-LoRa-HAT-Transmission-Communication/dp/B07W83FCCZ)  |
| Dragino | 868MHz version available | 30 USD | [Link](https://www.antratek.com/raspberry-pi-lora-gps-hat-868mhz) |
| Turta   | 433MHz & 868MHZ & 915MHz versions available |  60 USD | [Link](https://turta.io/collections/raspberry-pi-hats/products/lora-hat?variant=12549674958895) |


---


### **Type-2, LoRa Transceivers Modules**

- LoRa modules which can interface with the Raspberry-Pi board through UART\I2C\SPI

| Manufacturer | Operating Frequency | Price | Store Link |
| ------- |  -------- |  ----- | ----- |
| RAK-Wireless | 868MHz & 915MHz versions available | 25 USD | [Link](https://uk.pi-supply.com/products/rak813-lorab-ble5-and-lora-module-based-on-nrf52832-and-sx127x?_pos=15&_sid=30d832a4c&_ss=r)|
| RAK-Wireless | 433MHz & 868MHz & 915MHz versions available | 15 USD | [Link](https://uk.pi-supply.com/products/rak811-lora-lorawan-module?_pos=18&_sid=30d832a4c&_ss=r) |
| REYAX | 868MHz & 915MHz versions available | 20 USD | [Link](https://www.amazon.com/RYLR896-Module-SX1276-Antenna-Command/dp/B07NB3BK5H/ref=sr_1_1?dchild=1&keywords=LoRa&qid=1594195384&rnid=2941120011&s=pc&sr=1-1) |
| HopeRF  | 915MHz version available | 15 USD | [Link](https://www.amazon.com/RFM95W-915Mhz-Transceiver-SX1276-compatible/dp/B01F6HPWMC)|
| Aptinex | 433MHz & 868MHz versions available  | 35 USD | [Link](https://www.amazon.com/Aptinex-LoRaNode-RN2483A-Microchip-LoRaWAN/dp/B01N2RJPMJ/ref=sr_1_4?dchild=1&keywords=LoRa&qid=1594195384&rnid=2941120011&s=pc&sr=1-4) |
