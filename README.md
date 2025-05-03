# CalcBuild
I wanted to learn how to solder and design PCBs for some time and creating this calculator was a great opportunity to do so while also working on my CAD skills. This repository is here to have all my files and some pictures all in one place for easy access.

### Early Circuit Design
This is a numberpad I set up on a breadboard to test my code throughout the whole process of making the calculator. LCD uses the I2C protocol, I used libraries from a different github user to get it working properly.
![Image](./Images/IMG_7333.jpg)
 
### Schematic and PCB Design
After setting up the numberpad I got the general idea of how to set up the circuit so made a schematic.
![Image](./Images/image.png)

Final design of the PCB. Both the schematic and PCB were designed in Altium CircutMaker.
![Image](./Images/image-2.png)

### Finished PCB
![Image](./Images/IMG_7423.jpg)
![Image](./Images/IMG_7431.jpg)

### Case Model and Final Product
I directly exported the PCB and components from Altium into Fusion 360 to design the case.
![Image](./Images/CaseModel.png)

The calculator is powered by a AA battery pack behind the PCB that plugs into the Raspberry Pi Pico.
![Image](./Images/FullCalculator.jpg)

Really enjoyed working on this project! In the future I might try using a different microcontroller to reduce the size of the PCB and case since the battery pack is why the case is so thick. CAD, PCB and code files can be found above (code isnt the best but it gets the job done).
