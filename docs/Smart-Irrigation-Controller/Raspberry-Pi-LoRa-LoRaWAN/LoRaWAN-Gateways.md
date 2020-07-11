---
layout: post
parent: LoRa & LoRaWAN
title:  LoRaWAN Gateways
grand_parent : Smart Irrigation Controller
---
# Selecting our LoRaWAN Gateway

- To give internet access to our LoRaWAN nodes, we need them to connect to a main gateway.
-  **IMPORTANT :** Our gateway should operate on the ISM band EU433\EU868, as it is not legal to operate on other LoRaWAN ISM bands in Lebanon (such as US915). 

---



### **Type-1, Carrier-grade LoRaWAN Gateways** : 

- These models are intended for use with large-scale, commercial systems. 
- They require minimal set-up and can support large amounts of LoRaWAN nodes, but they are also the most expensive.


| Company | Model | # of Channels | Operating Frequency | Wi-Fi & Bluetooth | Price |
| -------------- | --------- | --------------------- | ------------------------------- | ----------------- | ------------- |
| Laird |  [Laird RG1xx Series](https://eu.mouser.com/new/laird-connectivity/laird-sentrius-rg1-lora-gateway/) | Up-to 8 channels | 868/915MHz Support | Supported | Not specified |
| Kerlink | [Kerlink iBTS](http://www.kerlink.com/en/products/lora-iot-station-2/wirnet-ibts) | Up-to 8 channels  |868/915MHz Support | Supported | Not specified |
| Lorix | [LORIX One](http://lorixone.io) |  Up-to 8 channels |868/915MHz Support | Supported | 500 USD |
| AAEON | [Aaeon UP](http://industrialgateways.eu/docs/) | Up-to 8 channels  |868/915MHz Support | Supported | 550 USD |
| Cisco | [Cisco LoRaWAN Gateway](https://www.cisco.com/c/en/us/products/routers/wireless-gateway-lorawan/index.html) |  Up-to 16 channels | 868/915MHz Support | Supported | 500 USD |
| Gemtek | All Gemtek models available [here](https://www.gemteks.com/en/products/lora-iot/gateway) |  Up-to 8 channels | 868/915MHz Support | Supported | Not specified |
| Tekletic | All Tektelic models available [here](https://tektelic.com/iot/lorawan-gateways/) | Up-to 8 channels  | 868/915MHz Support | Supported | Not specified |
| Ursalink | [UG87 Outdoor Gateway](https://www.ursalink.com/en/ug87-lorawan-gateway/) |  Up-to 8 channels | 868/915MHz Support | Supported |  Not specified |

---



### **Type-2, Pi-Hats**

- Pi-Hats modules are designed to be compatible with the GPIO interface of the Raspberry-Pi. 
- There are LoRaWAN Gateway Pi-Hats models available commercially. They are not sold bundled with Raspberry-Pi boards.
- This approach would offer a good compromise between price and setup complexity.

| Company | Model | # of Channels | Operating Frequency | Price |
| ------- | ----- | -------- | ---------- | ------|
| Pi-Supply | [LoRa Gateway HAT for Raspberry Pi](https://www.thethingsnetwork.org/marketplace/product/iot-lora-gateway-hat-for-raspberry-pi-868-mhz) | Up-to 8 channels | 868\915MHz Support | Around 160 USD|
| Adafruit | [LoRa Gateway Hat - SX1301 Based](https://www.adafruit.com/product/4284) | Up-to 8 channels | 915MHz Support | 150 USD |
| RAK-Wireless | [RAK2245 RPi HAT Edition](https://store.rakwireless.com/products/rak2245-pi-hat?variant=26653392502884)| Up-to 8 channels | 868MHz Support | 120 USD |

---



### **Type-3, Full-Enclosed Raspberry-Pi systems**

- Fully-Enclosed systems, containing a Raspberry-Pi board and LoRaWAN gateway module, along with additional accessories.
- Good compromise between price and setup complexity, if we account that it comes bundled with a pre-configured Raspberry-Pi board.

| Company | Model | # of Channels | Operating Frequency | Price |
| -------------- | --------- | --------------------- | ------------------------------- | ----------------- |
| Sparkfun | [LoRa Raspberry-Pi Gateway with Enclosure](https://www.sparkfun.com/products/15336) | Up-to 8 channels | 915MHz support | 200 USD |
| IMST | [LoRaWAN Gateway Platform](https://shop.imst.de/wireless-modules/lora-products/36/lite-gateway-demonstration-platform-for-lora-technology) | Up-to 8 channels | 868MHz | Around 230 USD |

---


### **Type-4, Custom LoRaWAN gateway**



- Cheapest option, but also the most complex. 
- We could order LoRaWAN gateway modules, such as the *IC880A-SPI*, which has an operating frequency of 868MHz and supports 8 channels. Extensive documentation is also available online.
- We would have to tinker with the hardware, and write code to configure how the Raspberry-Pi and the module communicate using the *UART* \ *SPI* \ *I2C* interface.
- Guide on setting up a LoRaWAN gateway using a Raspberry-Pi and a IC880A-SPI concentrator board is available [here](https://github.com/ttn-zh/ic880a-gateway/wiki). 
- Expected total price (Raspberry-Pi + IC880A-SPI) is 170 USD.
- Open-source *C* code, which we could use to configure the LoRaWAN gateway module, has been made available by Semtech [here](https://github.com/Lora-net/lora_gateway). Semtech designs almost all commercially available LoRaWAN gateway modules.



# Source : 

[The Things Network - Commercially Available LoRaWAN Gateways ](https://www.thethingsnetwork.org/docs/gateways/start/list.html)