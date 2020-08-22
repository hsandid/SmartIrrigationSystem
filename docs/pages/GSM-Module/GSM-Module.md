---
title: "Selecting a GSM Module"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: selecting-a-gsm-module.html
folder: GSM-Module
---

- To allow our Raspberry-Pi board to receive\transmit data over cellular network, we must equip it with a GSM transceiver.
- All models listed here require a SIM card with an active mobile broadband subscription.
- A reference to the Lebanese National Frequency allocation Table can be found [here](http://www.tra.gov.lb/Library/Files/Uploaded%20files/LNFT_TRA_Final%20Version%20for%20publication_24062008.pdf). It contains all information related to the bands occupied by mobile traffic & data services in Lebanon.
- Here is a reference of cellular network technologies and their associated bandwidth speed :

![Cellular Technologies](../../images/Table-Cellular-Technology-Speed.PNG)

---



### **Type-1, Pi-Hat GSM Module:**

- Pi-Hats modules are designed to be compatible with the GPIO interface of the Raspberry-Pi.
- **IMPORTANT** : How many pins does each Pi-Hat model require ? If the Pi-Hat uses too much pins, we might not be able to connect the Raspberry-Pi to other components (i.e. flow meters, LoRa modules...).

| Manufacturer |  Price   | Store Link  |
| ------------ | ----------| ------------------------------------------------------------ |
| WaveShare | 23 USD | [Link](https://www.waveshare.com/sim800c-gsm-gprs-hat.htm)|
| Adafruit | 40 USD | [Link](https://learn.adafruit.com/fona-tethering-to-raspberry-pi-or-beaglebone-black) |

---

### **Type-2, GSM Module**

- General purpose modules that communicate over UART\I2C\SPI

| Manufacturer |  Price   | Store Link  |
| ------------ | ----------| ------------------------------------------------------------ |
| SIMCOM | 15 USD (Module Only) | [Link](https://www.amazon.com/SIM800L-Wireless-Module-Quad-Band-Antenna/dp/B07SY9QVRT) |
|SIMCOM | 20 USD | [Link](https://www.amazon.com/Nobrand-Development-Module-Suitable-Antenna/dp/B085MQGD64/ref=sr_1_8?dchild=1&keywords=sim900&qid=1595387285&s=electronics&sr=1-8)|

---

### **Type-3, 4G USB Dongle**

- The Raspberry-Pi supports USB dongle. We can buy one locally from the main telecommunications companies (i.e. Alfa\MTC).
- Prices of dongles are ambiguous due to them being listed in dollars (Do Alfa & MTC respect the 1515LBP\USD rate ?). Full list available here : [Alfa Store](https://www.alfa.com.lb/en/devices-accessories/dongles-routers/about) - [MTC Store](https://www.touch.com.lb/autoforms/portal/touch/personal/internet-offers/highspeedinternet/4g-devices)

- Mobile Broadband bundles
  - All Alfa Mobile Broadband plans are available [here](https://www.alfa.com.lb/en/mobile-broadband/about)
  - All MTC Mobile Broadband plans are available [here](https://www.touch.com.lb/autoforms/portal/touch/personal/internet-offers/residentialbroadband/tariffs)

# Source 

- [Ken's Tech Tips - Cellular Networks Technologies](https://kenstechtips.com/index.php/download-speeds-2g-3g-and-4g-actual-meaning)