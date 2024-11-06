import speech_recognition as sr
from pyfirmata import Arduino, SERVO, util
from time import sleep

r=sr.Recognizer()
mic = sr.Microphone(device_index=1)

port = 'COM4'
pin1 = 13
pin2 = 12
pin3 = 11
pin4 = 10
pin5 = 9

board = Arduino(port)

board.digital[pin1].mode=SERVO
board.digital[pin2].mode=SERVO
board.digital[pin3].mode=SERVO
board.digital[pin4].mode=SERVO
board.digital[pin5].mode=SERVO

def rotate(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.01)
    
with mic as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = r.listen(source)
        try:
            if r.recognize_google(audio) =='first finger':
                print("switch is on")
                for i in range(0,360):
                    rotate(pin1,i)

            
            elif r.recognize_google(audio) =='middle finger':
                print("switch is on")
                for i in range(0,360):
                    rotate(pin2,i)


            elif r.recognize_google(audio) =='ring finger':
                print("switch is on")
                for i in range(0,360):
                    rotate(pin3,i)


            elif r.recognize_google(audio) =='small finger':
                print("switch is on")
                for i in range(0,360):
                    rotate(pin4,i)

            
            elif r.recognize_google(audio) =='fat finger':
                print("switch is on")
                for i in range(0,360):
                    rotate(pin5,i)
            else:
                print("something")
        
        except:
            print("no audio")
