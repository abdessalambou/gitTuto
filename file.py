"""This document contain function that allows us to control car
"""
#import RPi.GPIO as GPIO
from time import sleep
# GPIO used to control the first motor
INPUT1 = 24
INPUT2 = 23
ENABLE_A = 25
# GPIO used to control the second motor
INPUT3 = 17
INPUT4 = 27
ENABLE_B = 18
# Motor direction (1 for backward, -1 for forward, 0 car stopped)
motorDirection=1

print('\n')
print('The default speed & direction of motor is LOW & Forward.....')
print('r-run s-stop f-forward b-backward l-low m-medium h-high tr-turn right tl-turn left e-exit')
print('\n')
def forward():
    """This function allows the car to move forward
    """
    print('forward')
    motorDirection=1
    userInput='z'
def backward():
    """This function allows the car to move backward
    """
    print('backward')
    motorDirection=-1
    userInput='z'
def stopCar():
    """This function allows us to stop the car
    """
    print('stop')
    motorDirection=0
    userInput='z'
def turnRight():
    """This function allows to turn the car right
    """
    print('turn right')
    motorDirection=1
    userInput='z'
def turnLetf():
    """This function allows to turn the car left
    """
    print('turn left')
    motorDirection=1
    userInput='z'
def slowDownCar():
    """This function allows to slow down car
    """
    print('low')
    userInput='z'
def speedUpCar():
    """This function allows to speed up car
    """
    print('high')
    userInput='z'
def mediumUpCar():
    """This function allows to medium up car
    """
    print('medium')
    userInput='z'
# This loop allows to control the car using the keyboard
while True :
    # Read user's input from keyboard
    userInput=input()
    if userInput=='r':
        print('run')
        if motorDirection==1 :
            forward()
        elif motorDirection==-1:
            backward()
        else:
            stopCar()
    # If user types 's', stop the car
    elif userInput=='s':
        stopCar()
    # If user types 'f', run the car to forward
    elif userInput=='f':
        forward()
    # If user types 'tr', turn the car to right
    elif userInput=='tr':
        turnRight()
    # If user types 'tl', turn the car to left
    elif userInput=='tl':
        turnLetf()
    # If user types 'b', run the car to backward
    elif userInput=='b':
        backward()
    # If user types 'l', slow down the car
    elif userInput=='l':
        slowDownCar()
    # If user typs 'm', medium up the car
    elif userInput=='m':
        mediumUpCar()
    # If user types 'h', speed up the car
    elif userInput=='h':
        speedUpCar()
    # If user types 'e', clean up the GPIO pins and exit the program
    elif userInput=='e':
        print('GPIO Clean up')
        break
    # If user types an invalid command, display an error message
    else:
        print('<<<  wrong data  >>>')
        print('please enter the defined data to continue.....')
