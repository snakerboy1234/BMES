import RPi.GPIO as GPIO
import random
import time

def main():
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(5, GPIO.IN)
    GPIO.setup(13, GPIO.IN)
    GPIO.setup(20, GPIO.IN)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

    Continue = 1
    x = 3
    buttonPressed = 0

    listOfNumbers = []
    userListOfNumber = []

    random.seed(1)
    
    while(Continue == 1):
        
        generateNextInput(listOfNumbers)
        printGeneratedNumbers(listOfNumbers)
        
        i = 0
        
        while(i < len(listOfNumbers)):
            searchForPress(userListOfNumber)
            i = i + 1
        
        GPIO.output(27, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        checkAnswers(userListOfNumber, listOfNumbers, Continue)
        userListOfNumber = []
    
    
    
def generateNextInput(listOfNumbers):
    
    rand = random.randrange(0, 4, 1)
    
    listOfNumbers.append(rand)
    
    print(*listOfNumbers)
    
    return 0

def printGeneratedNumbers(listOfNumbers):
    
    i = 0

    while(i < len(listOfNumbers)):
        if(listOfNumbers[i] == 0):
            GPIO.output(27, GPIO.HIGH)
            time.sleep(.50)
            GPIO.output(27, GPIO.LOW)
        elif(listOfNumbers[i] == 1):
            GPIO.output(6, GPIO.HIGH)
            time.sleep(.50)
            GPIO.output(6, GPIO.LOW)
        elif(listOfNumbers[i] == 2):
            GPIO.output(26, GPIO.HIGH)
            time.sleep(.50)
            GPIO.output(26, GPIO.LOW)
        elif(listOfNumbers[i] == 3):
            GPIO.output(21, GPIO.HIGH)
            time.sleep(.50)
            GPIO.output(21, GPIO.LOW)
        else:
            print('Error')
        
        i= i + 1
    
    return 0

def searchForPress(userListOfNumber):

    CONST_BLUE_BUTTON = 17
    CONST_RED_BUTTON = 5
    CONST_WHITE_BUTTON = 13
    CONST_GREEN_BUTTON = 20

    while True:
        if(GPIO.input(CONST_BLUE_BUTTON) or GPIO.input(CONST_RED_BUTTON) or GPIO.input(CONST_WHITE_BUTTON) or GPIO.input(CONST_GREEN_BUTTON)):
            break
        else:
            pass

    identifyButtonPressed(userListOfNumber)

    time.sleep(1)

    while True:
        
        if( (not GPIO.input(CONST_BLUE_BUTTON)) and (not GPIO.input(CONST_RED_BUTTON)) and (not GPIO.input(CONST_WHITE_BUTTON)) and (not GPIO.input(CONST_GREEN_BUTTON)) ):
            break
    
    time.sleep(.50)
    
    while True:
        
        if( (not GPIO.input(CONST_BLUE_BUTTON)) and (not GPIO.input(CONST_RED_BUTTON)) and (not GPIO.input(CONST_WHITE_BUTTON)) and (not GPIO.input(CONST_GREEN_BUTTON)) ):
            break
    
    return 0

def identifyButtonPressed(userListOfNumber):

    CONST_BLUE_BUTTON = 17
    CONST_RED_BUTTON = 5
    CONST_WHITE_BUTTON = 13
    CONST_GREEN_BUTTON = 20

    pressedButton = 0

    if(GPIO.input(CONST_BLUE_BUTTON)):
        pressedButton = 0
        GPIO.output(27, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(27, GPIO.LOW)
        addButtonPress(pressedButton, userListOfNumber)

    elif(GPIO.input(CONST_RED_BUTTON)):
        pressedButton = 1
        GPIO.output(6, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(6, GPIO.LOW)
        addButtonPress(pressedButton, userListOfNumber)

    elif(GPIO.input(CONST_WHITE_BUTTON)):
        pressedButton = 2
        GPIO.output(26, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(26, GPIO.LOW)
        addButtonPress(pressedButton, userListOfNumber)

    elif(GPIO.input(CONST_GREEN_BUTTON)):
        pressedButton = 3
        GPIO.output(21, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(21, GPIO.LOW)
        addButtonPress(pressedButton, userListOfNumber)

    else:
        print('Possible error')
        addButtonPress(listOfNumbers)

    return 0

def addButtonPress(pressedButton, userListOfNumber):
    
    userListOfNumber.append(pressedButton)

    return 0

def checkAnswers(userListOfNumber, listOfNumbers, Continue):
    
    print(*userListOfNumber)
    
    if(userListOfNumber == listOfNumbers):
        print('good')
        Continue = 1

    else:
        print('bad')
        Continue = 0
        exit()

    return 0

main()