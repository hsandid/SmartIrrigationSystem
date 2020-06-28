---
layout: post
title:  "Internship Meeting, Week #3 (June 23)"
---

- Work Completed this week :

  - Added map interface to the S.I.C. web interface. Found [here](https://github.com/hsandid/SmartIrrigationSystem/tree/master/WebInterface).
  - Added registration process to the S.I.C. web interface. Found [here](https://github.com/hsandid/SmartIrrigationSystem/tree/master/RegistrationProcess).
  - Set-up a web server on the Raspberry-Pi board, using *Apache*.

### Smart Irrigation Controller - Web Interface

- Discuss the newly-added map interface
- Discuss the newly-added registration process
- Current Python scripts are redundant with the web interface. Implement python scripts which runs continually in the background
- **Important** : Re-discuss the "Irrigation Control Method" from last meeting, and clarify how it should be implemented. How much will we rely on algorithms to control the irrigation routine ? How much control should we give to the user ?

### Enclosure

 - Looking for an enclosure which can be used. Any local producer, so we don't have to import it ? More details [here](https://gist.github.com/hsandid/71a9572bae61ed78697474a847df5c54).

### Upcoming Report

- Raspberry-Pi 3 Model B Hardware \ Interfaces \ Power & Voltage & Current Limitations.
- Raspberry-Pi Zero Hardware \ Interfaces \ Power & Voltage & Current Limitations.
- Linux distribution to use, if we are going to ship a product out commercially (i.e. Legal Issues, and lightweight distribution).
- Power supply solutions to make the Rasp. Pi portable using external batteries and solar power. 
- Requirements of the LoRa interface, especially when connected with a Raspberry-Pi.


### Meeting Questions

- Meeting with agriculture experts ?
- Obtaining the LoRa interface ?
- Might have to borrow some tools/parts from the FEA labs. How can I contact them & reach them ? Do I need special access ?
- Google Cloud access for testing ? Possible alternatives (using GitHub pages, etc...).
