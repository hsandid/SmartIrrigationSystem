---
layout: post
parent: PCB Design
title:  Schematic and PCB Layout V1
nav_order : 2
grand_parent : Smart Irrigation Controller
---

# Schematic and PCB Layout

- Complete KiCad project (including schematics, footprints and layouts) is available [here](../../../assets/zip/SmartIrrigationController-V1.zip).
- For this implementation, we've used the UART interface of the Raspberry-Pi (GPIO Pins #14 and #15), two additional GPIO Pins to control elements of the circuit ( GPIO Pins #22 and #23 ), a 3v3 output power pin, and a ground pin.
- There are still 24 available GPIO pins, which can be used to control additional modules. The SPI & I2C interfaces are also fully available, if we'd like to use them with other modules.

# Schematic Circuit

![Schematic](../../../assets/images/PCB-Diagram.svg)

# PCB Layout

Front Layer :

![Front Layer PCB](../../../assets/images/PCB-Layout-Front.PNG)

Back Layer :

![Back Layer PCB](../../../assets/images/PCB-Layout-Back.PNG)

3D View :

![3D View #1](../../../assets/images/PCB-3D-1.png)
![3D View #2](../../../assets/images/PCB-3D-3.png)
![3D View #3](../../../assets/images/PCB-3D-2.png)