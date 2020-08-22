---
title: "Meeting #2 - June 15th"
keywords: 
last_updated: 
tags: 
sidebar: meetings_sidebar
permalink: Meeting-15thJune.html
folder: meetings
---

### Work Completed during this Week

- Web Interface prototype, for the Raspberry-Pi



### Deploying a Raspberry-Pi prototype in the field


I need to conduct a feasibility study before moving on to the implementation.

- Enclosure for the Raspberry-Pi to protect it when deployed outdoors on agricultural fields (i.e. bad weather, physical shock...).
- Find a way to power the Raspberry-Pi device efficiently in the field. ( Portable battery pack ? Solar Power ? )
- Meeting with experts from the agriculture department
   - What irrigation systems (i.e. pumps, actuators...) should I expect the *Smart Irrigation Controller* to interact with ? Is it possible to design a universal system which is compatible with all common irrigation systems (both hardware/software) ?


### Code Review

We must agree on a time to conduct a code review for the Raspberry-Pi scripts and web interface, and also the Mobile application.


### Post-Meeting Decisions

- Add a map to the web interface, so the user can see his field(s).
- Add a registration process to the S.I.C. web interface
- Set-up a lightweight web-server to host the web irrigation interface on the Raspberry-Pi
- Re-discuss the irrigation control methods, and how we should approach a manual/automatic scheduling.