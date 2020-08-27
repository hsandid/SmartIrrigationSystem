---
title: "PCB Design Rules"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: PCB-Design-Rules.html
folder: Raspberry-Pi-Model-Information
---

Here are some general recommendations concerning PCB Design, especially two-layer PCBs :

### Component Placement 

- Similar components should be oriented in the same direction. It is recommended to use annotations on the PCB's silkscreen to indicate each component's orientation, as it facilitates the soldering process.
- It is recommended to place all SMD/TH components on a single side of the board to facilitate soldering. Also, avoid placing SMD components in proximity to the solder side of through-hole components.
- Consider which components dissipate the most heat on a design ( which can be accomplished used the "Thermal Resistance" ratings in the components' datasheets). Follow guidelines to divert heat, and use heatsinks and cooling fans when necessary. If the PCB contains multiple components producing large amount of heat, it is recommended to spread them across the board. Use Thermal Reliefs when necessary ( [Thermal Reliefs on Wikipedia](https://en.wikipedia.org/wiki/Thermal_relief)).

### Power, Ground and Signal Traces

- For two-layer boards, we usually have a ground plane and rely on tracks to deliver power from a power source.
- Net width depends on the expected amount of current which will flow through. Most low-current analogue and digital signals can function on the recommended width of 0.010 inches. PCB Traces, which are expected to carry more than 0.3A, should be wider. A trace width calculator is available [here](http://www.4pcb.com/trace-width-calculator.html) to calculate the recommended net width.

- For Integrated Circuits (i.e. ICs), it is recommended to use common rails (i.e. COMs, which is a shared path between different electrical routes in an electrical circuit), and to avoid daisy-chaining between components.


### EM & RF Constraints 

- **Transmission line** : 
  - At low frequencies, small tracks can be considered purely by their DC characteristics. However as frequencies rise, the track starts behaving like a transmission line, with a characteristic capacitive/inductive impedance. 
  - We can calculate the impedance of the line from a combination of line thickness, distance between line and ground plane, and the dielectric constant of the board. 
  - Placing tracks behaving like transmission lines close to the ground helps them maintain the same characteristic impedance (See *Crosstalk* section). 
  - If a track acting as a TL passes between layers, we must take into consideration that its distance to the ground plane will change. We can ensure that the line impedance remains the same by modifying the line thickness of a track when it transitions to another layer.
- **Impedance Matching** : 
  - If a track acts as a transmission line, the impedance must be matched between the line and the load if a track. If there is a mismatch between the line and the load, not all energy of the waveform is absorbed by the load, and this unabsorbed energy might be reflected back, causing interference. 
  - We must match the TL to the line driver/transmitter and the line receivers. We can either use drivers and receivers with appropriate impedance, or use a resistor down to ground to obtain matching impedances. If we were to use drivers, their capability must be higher than logic-only chips and special line drivers should be use to supply the current required to drive the lines. 
  - We can use clamping diodes to control the level of overshoot or undershoot, and maintain signal integrity. However, having proper impedance matching yields far better results.
- **Crosstalk** : 
  - Signals from one line can also appear on nearby lines, which harms signal integrity. This can be caused by either mutual inductance or mutual capacitance. 
  - Mutual inductance is the effect that is used in transformers. It arises from the fact that a current in one track sets up a magnetic field. Changes in this field then induce a current in a nearby track. 
  - Mutual capacitance occurs as a result of the coupling of the electric fields between two tracks. A voltage appearing on one track creates an electric field which can couple to a second line. Changing voltages,  especially fast edges can result in similar edges appearing on nearby lines. 
  - To avoid these effects, we should avoid tracks that run in parallel on any adjacent layers, if tracks have to cross, they should cross at right angles and using layers as far apart as possible. Line spacing should be as wide as possible, and to reduce mutual  capacitance lines should be as thin as possible. Finally, where transmission lines are used, they should be as close to the ground plane as possible. This will reduce coupling to other nearby lines.

**Simultaneous switching** : 

- If several output lines are switched simultaneously, the transient currents become very large, and this can give rise to signal instability. Signal integrity issues arise because a voltage arises between the device ground and the board ground. 
- If the chip ground rises sufficiently it can cause the signal switching levels to be exceeded, thereby causing spurious switching to occur. A workaround would be to avoid simultaneous switching in the circuit. 
- If the circuits are operated synchronously and we cannot avoid simultaneous switching, we should at least ensure that we have a good grounding to avoid signal instability.

# Source 

- [Altium -  PCB Design Recommendations](https://resources.altium.com/p/top-5-pcb-design-guidelines-every-pcb-designer-needs-know)
- [Electronics-Notes - PCB Design Recommendations](https://www.electronics-notes.com/articles/analogue_circuits/pcb-design/pcb-design-layout-guidelines.php)
- [Quick-PCBA - PCB Design Tips](https://www.quick-pcba.com/pcb-news/why-not-odd-number-multilayer-printed-circuit-board.html)

