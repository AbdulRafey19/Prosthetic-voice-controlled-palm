# Prosthetic Voice Controlled Palm

![image](https://github.com/user-attachments/assets/048a9497-61e8-4f4b-8a32-26e00000ad95)

This project helps build a simple code in python to controll the movement of servos using voice commands. The picture above showcases the final assembly and look of the prosthetic palm.

## Compoennts Required
1. Arduino UNO
Arduino is used to send the signal to the servos.
![image](https://github.com/user-attachments/assets/7a14a091-3420-483c-b25d-50b3bc436b02)

2. Servos 
Servos are used to control the movement of each finger
![image](https://github.com/user-attachments/assets/2b013056-74b4-403b-b76b-d945a58fdfd3)

3. Breadboard 
Breadboard is used to build semi-permanent prototype of the projects circuit. 
![image](https://github.com/user-attachments/assets/f0239190-10d7-44f6-8f5d-87ceb9c0c799)

## Mechanical CAD setup for the prosthetic hand
The mechanical aspect and the structure of the prosthetic hand was designed using SolidWorks. The cad was 3d printed on a material called PLA. Each individual part was 3d printed and then assembled together to form the palm.

The additional materials used for connecting the fingers to the main hand were nylon threads, double-sided tape, a wooden platform, and zip tiles to complete the prosthetic hand mechanically. Following are the screenshots of the stl files for every individual part of the hand:
1. Palm:
![image](https://github.com/user-attachments/assets/f44be33d-413f-4c5f-8c80-9b62f293f651)

2. Finger Bottom
![image](https://github.com/user-attachments/assets/92b2b679-0d3d-482e-9fb6-eba72632a718)

3. Finger Top
![image](https://github.com/user-attachments/assets/77b6f71b-8b60-403f-ae74-5d700850bf9c)

4. Thumb Bottom
![image](https://github.com/user-attachments/assets/9b9c758f-a8ff-4d60-9abe-abba69bf0178)

5. Thumb Top
![image](https://github.com/user-attachments/assets/97e8f712-3919-404f-b096-60e683e1fe4c)

## Arduino Connection With Servo
![image](https://github.com/user-attachments/assets/c59144f9-5ec9-4779-870f-6c740a247478)
There are 5 servos which will all be powered using breadboard. And the signal wire of each servo will be attached with the Arduino output pins.

## Working
pyfirmata, an Arduino library, is used to control the movements of the servo. This library was integrated into visual studio and using python programming signal were sent from computer to the Arduino in order to control the servos. A microphone is used to hear the users commands which will be processed by the  python code running on the computer and then a signal is sent to the Arduino upon hearing a successful command and the Arduino will then move the desired servos.
