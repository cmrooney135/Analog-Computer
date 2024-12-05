# Analog Computer for Solving Non-Linear Differential Equations

The following details the project in which an analog computer was designed to solve the predator-prey equation. This solution involved programming an ESP32-C3-DevKitM-1U to collect data and switch channels. 
There is also a software component with a GUI that allows the user to set initial conditions for the equation and edit the parameters. 


## File Structure 

The software for the gui and the code for the microcontroller is in the folder [main](main). 

ESP-IDF projects are built using CMake. The project build configuration is contained in `CMakeLists.txt`
files that provide set of directives and instructions describing the project's source files and targets
(executable, library, or both). 

Below is short explanation of remaining files in the project folder.

```
├── CMakeLists.txt
├── main
│   ├── CMakeLists.txt
│   └── main.c
└── README.md                  This is the file you are currently reading
```
Additionally, the sample project contains Makefile and component.mk files, used for the legacy Make based build system. 
They are not used or needed when building with CMake and idf.py.
