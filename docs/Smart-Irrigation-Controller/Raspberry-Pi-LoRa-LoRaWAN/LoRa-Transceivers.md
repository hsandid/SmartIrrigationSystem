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
- There are many LoRa transceiver Pi-Hats models available commercially.

| Manufacturer  | Operating Frequency | Price | Store Link |
| ------- |  -------- |  ----- | ----- |
| Pi Supply | 433\868MHz Support | 150 USD | [Link](https://uk.pi-supply.com/products/iot-lora-node-phat-for-raspberry-pi?_pos=41&_sid=30d832a4c&_ss=r)|
| IoT Store | 433\868MHz Support | 60 USD | [Link](https://www.iot-store.com.au/products/lora-and-gps-hat-for-raspberry-pi-long-range-transceiver) |
| Waveshare  | 915MHz Support | 35 USD | [Link](https://www.amazon.com/SX1262-LoRa-HAT-Transmission-Communication/dp/B07W83FCCZ)  |
| Dragino | 868MHz Support | 30 USD | [Link](https://www.antratek.com/raspberry-pi-lora-gps-hat-868mhz) |
| Turta   | 433\868MHz Support |  60 USD | [Link](https://turta.io/collections/raspberry-pi-hats/products/lora-hat?variant=12549674958895) |

---


### **Type-2, LoRa Transceivers Modules**

- LoRa modules which can interface with the Raspberry-Pi board through UART\I2C\SPI

| Manufacturer | Operating Frequency | Price | Store Link |
| ------- |  -------- |  ----- | ----- |
| RAK-Wireless | 433\868MHz Support | 25 USD | [Link](https://uk.pi-supply.com/products/rak813-lorab-ble5-and-lora-module-based-on-nrf52832-and-sx127x?_pos=15&_sid=30d832a4c&_ss=r) + [Breakout Board](https://www.amazon.co.uk/Location-Tracker-breakout-LoRaWAN-Bluetooth/dp/B07P3LRYQZ)|
| RAK-Wireless | 868\915MHz Support | 15 USD | [Link](https://uk.pi-supply.com/products/rak811-lora-lorawan-module?_pos=18&_sid=30d832a4c&_ss=r) + [Breakout Board](https://uk.pi-supply.com/products/rak811-breakout-board-sma-ipx-connectors?_pos=36&_sid=30d832a4c&_ss=r) |
| REYAX | 868\915MHz Support | 20 USD | [Link](https://www.amazon.com/RYLR896-Module-SX1276-Antenna-Command/dp/B07NB3BK5H/ref=sr_1_1?dchild=1&keywords=LoRa&qid=1594195384&rnid=2941120011&s=pc&sr=1-1) |
| HopeRF  | 915MHz Support | 15 USD | [Link](https://www.amazon.com/RFM95W-915Mhz-Transceiver-SX1276-compatible/dp/B01F6HPWMC) + [Breakout Board](https://www.amazon.com/Adafruit-RFM95W-Radio-Transceiver-Breakout/dp/B01HYO608A/ref=sr_1_2?dchild=1&keywords=LoRa&qid=1594195384&rnid=2941120011&s=pc&sr=1-2) |
| Aptinex | 433\868MHz Support  | 35 USD | [Link](https://www.amazon.com/Aptinex-LoRaNode-RN2483A-Microchip-LoRaWAN/dp/B01N2RJPMJ/ref=sr_1_4?dchild=1&keywords=LoRa&qid=1594195384&rnid=2941120011&s=pc&sr=1-4) |