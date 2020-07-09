---
layout: post
parent: Portable Power Solution
title:  Theory
grand_parent : Smart Irrigation Controller
---

- Raspberry-Pi requires 5V/2.5A to be supplied to its micro-USB port.
- We could plug our board to a local power source (i.e. electric grid or any electric generator) which delivers 5V/2.5A. However, this limits the portability of our *Smart Irrigation Controller*
- We could find a more portable solution to power our Raspberry-Pi.
- Using batteries only would allow our system to be portable, but we would also have to take care of replacing batteries on a regular basis.
- Another option would be to use rechargeable batteries,  which could be recharged automatically without needing to be connected to the local grid or electric generators.
- We could provide power for the rechargeable batteries by using a renewable energy source, such as solar energy

![image info](../../../assets/images/Diagram-Solar-Energy.PNG)

- Raspberry-Pi 3 B at maximum CPU load consumes around 3.7W
  - Assuming our board is active 24/7, it would consume <img src="https://render.githubusercontent.com/render/math?math=3.7*24 = 88.8"> Wh/Day
  - We would require our battery to be able to store/provide around 100 Wh/Day
  - We would require a solar panel with enough voltaic cells to support our 100 Wh/Day battery. This would correspond to a small form factor solar panel able to provide 5W or 120Wh/Day
- Raspberry-Pi Zero at maximum CPU load consumes around 0.7W
  - Assuming our board is active 24/7, it would consume <img src="https://render.githubusercontent.com/render/math?math=0.7*24 = 16.8"> Wh/Day
  - We would require our battery to be able to store/provide around 20 Wh/Day
  - We would require a solar panel with enough voltaic cells to support our 20 Wh/Day battery. This would correspond to a small form factor solar panel able to provide 1W or 20Wh/Day

### Practical Example

If possible with the current situation, it would be interesting to obtain a small form-factor solar panel and batteries to test this portable setup for the *Smart Irrigation Controller*