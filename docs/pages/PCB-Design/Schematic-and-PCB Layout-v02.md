---
title: "Schematic and PCB Layout (V02)"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: PCB-Schematic-Layout-V02.html
folder: PCB-Design
---

- Complete KiCad project (including schematics, footprints and layouts) is available [here](../../zip/SmartIrrigationController-V2.zip).
- For this implementation, we've used the UART interface of the Raspberry-Pi (GPIO Pins #14 and #15), two additional GPIO Pins to control elements of the circuit ( GPIO Pins #22 and #23 ), a 3v3 output power pin, and a ground pin.
- There are still 24 available GPIO pins, which can be used to control additional modules. The SPI & I2C interfaces are also fully available, if we'd like to use them with other modules.

# Schematic Circuit

![Schematic](../../images/PCB-Diagram-V2.PNG)

# PCB Layout

Front Layer :

![Front Layer PCB](../../images/PCB-Layout-Front-v2.png)

Back Layer :

![Back Layer PCB](../../images/PCB-Layout-Back-v2.png)

3D View :

![3D View #1](../../images/PCB-3D-V2-1.png)