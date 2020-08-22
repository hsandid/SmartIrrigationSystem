---
title: "BOM for our PCB Design (V01)"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: PCB-BOM-v01.html
folder: PCB-Design
---

- LoRaWAN Gateway System, operating on EU868 ISM Band (2pc)
- LoRa Transceiver, UART Compatible & operating on EU868 ISM Band (3pc)
- 868MHz U.FL Antenna for the LoRa Transceiver (3pc)
- GSM Module, UART Compatible & operating on Lebanese 2G/GSM (i.e frequency 900MHz) (3pc)
- 900MHz U.FL Antenna for the GSM Module (3pc)
- Demultiplexer (2:1) (2pc)
- 40 Pins Male Connector (3pc)
- 40 Pins Female Connector (3pc)

## LoRa UART\SPI Transceiver 

- Name : MTXDOT-EU1-A00-1
- Dimensions : 23.62 x 23.62 x 3.51 mm ( Length x Width x Height )
- Operating Frequency : 868MHz
- Serial Interfaces : UART, SPI and I2C
- Operating Voltage : 2.4 to 3.57 V ( We can use a 3V3 pin on the Pi)
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/multi-tech-systems-inc/MTXDOT-EU1-A00-1/591-1292-ND/6237035)
- Datasheet [Link](https://www.multitech.com/documents/publications/manuals/s000645.pdf)

## Antenna Connector for LoRa 868MHz

- Name : ANT-868-SP
- Dimensions :  27.94 x 13.7 x 1.5 mm ( Length x Width x Height )
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/linx-technologies-inc/ANT-868-SP/ANT-868-SP-ND/340128)
- Datasheet [Link](https://linxtechnologies.com/wp/wp-content/uploads/ant-868-sp.pdf)

---

## GSM UART Module

- Name : NL-SW-GPRS
- Protocol : 2G/3G GPRS/GSM
- Frequencies : 850MHz, 900MHz, 1.8GHz, 1.9GHz 
- Dimensions : 29.0 x 33.60 x 6.63 mm
- Serial Interface : UART
- Antenna included ? : No
- Operating Votage : 3.5V ~ 4.3V 
- Current - Receiving : 330mA 
- Current - Transmitting : 330mA 
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/nimbelink-llc/NL-SW-GPRS/1477-1003-ND/4573470)
- Datasheet [Link](https://nimbelink.com/Documentation/Skywire/2G_GPRS/30007_NL-SW-GPRS_Datasheet.pdf)

## Antenna Connector for GSM Module

- Name : TG.30.8113 
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/taoglas-limited/TG.30.8113/931-1213-ND/3724547)
- Datasheet [Link](https://cdn.taoglas.com/datasheets/TG.30.8113.pdf)

---

## Demultiplexer

- Name : 74LVC1G18GW,125
- Dimensions : 2.2 x 2.2 x 1.1 mm ( Length x Width x Height )
- Operating Voltage : 1.65V ~ 5.5V 
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/nexperia-usa-inc/74LVC1G18GW-125/1727-6071-1-ND/2753907)
- Datasheet [Link](https://assets.nexperia.com/documents/data-sheet/74LVC1G18.pdf)

---

## Connector Pin Female 40-Pins

- Name : PPTC202LFBN-RC 
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/sullins-connector-solutions/PPTC202LFBN-RC/S6104-ND/807240)
- Datasheet [Link](https://media.digikey.com/pdf/Data%20Sheets/Sullins%20PDFs/Female_Headers.100_DS.pdf)

---

## Connector Pin Socket 40-Pins

- Name : PPTC202LFBN-RC 
- DigiKey Store [Link](https://www.digikey.com/product-detail/en/sullins-connector-solutions/PPTC202LFBN-RC/S6104-ND/807240)
- Datasheet [Link](https://media.digikey.com/pdf/Data%20Sheets/Sullins%20PDFs/Female_Headers.100_DS.pdf)

---

# TBD

- Connector Header with 40-pins 
- Current Limiting Resistors (Must account for 3V3 and 5V supplies on the Raspberry-Pi GPIO header).
- Battery\Solar Panel system connected to the PCB
- EEPROM memory, so it has an ID to identify the board.