## ROADM (Reconfigurable Optical Add-Drop Multiplexer)  Development

This project focuses on the development of an ROADM (Reconfigurable Optical Add-Drop Multiplexer) switch device. All requirements are defined in each LAB folder, which outlines each step needed to reach the final solution. A series of experiments was performed to evaluate the system, including the following measurements:

- Total network capacity
- Per-link average capacity & GSNR
- Per-link minimum/maximum capacity & GSNR
- Blocking event count

This is the assigned network topology.
![Network Diagram](https://github.com/carmenmoncada/Open_Optical_Network_Project/blob/main/presentation_final.jpg)

To run each part of the project separately (Lab01, Lab02, and so on), open the main file in the 'Tasks' folder. For example:
```
lab3-network-carmenmoncada96
└── Lab3
    └── tasks
        ├── lab3_network_main.py
        ├── Lab_04.py
        ├── Lab_05.py
        └── Lab_06.py
```

To run the script with the final configuration and methodologies assigned, go to and select 'main_congestion_scenario.py' to run the network when there is not enough network capacity, or run 'main_lab09.py' to run the network with only 100 connections:

```
lab9-traffic-matrix-carmenmoncada96
└── Lab_09
    └── tasks
        ├── main_congestion_scenario.py
        ├── main_lab09.py
        └── main.py
```

All the necessary libraries and packages are in:
```
lab9-traffic-matrix-carmenmoncada96
└── Lab/site-packages
```

Enjoy!!
