import RPi.GPIO as GPIO
import random
'''
GPIO.setmode(GPIO.BCM)

#GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

i = 0
x = 3
buttonPressed = 0

listOfNumbers = []

random.seed(568)

rand = random.randrange(0, 3, 1)

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

    i = 0
    x = 3
    buttonPressed = 0

    listOfNumbers = []

    random.seed(568)

    rand = random.randrange(0, 3, 1)
    
    searchForPress()
'''
def printButton (button, w, listOfNumbers):
    
    blue = 0
    red = 1
    yellow = 2
    green = 3
    currentNumber = 0
    
    if(button == 17):
        print ("button 17. blue")
        button = blue
        currentNumber = currentNumber + 1
    if(button == 5):
        print("button 5, red")
        button = red
        currentNumber = currentNumber + 1
    if(button == 13):
        print("button 13, yellow")
        button = yellow
        currentNumber = currentNumber + 1
    if(button == 20):
        print("button 20, green")
        button = green
        currentNumber = currentNumber + 1
        
    checkForFollowThrough(button, currentNumber, listOfNumbers)
    
    return 0

def checkForFollowThrough(buttonPressed, currentNumber, listOfNumbers):
    if(buttonPressed == 0):
        return 99
    if(listOfNumbers[currentNumber] == buttonPressed):
        return 1
    else:
        return 0
        

def printGeneratedNumbers(listOfNumbers):
    
    iterator = 0
    lengthOfList = len(listOfNumbers)
    
    while(iterator < lengthOfList):
        print(listOfNumbers[iterator], end='')
        iterator = iterator + 1
    
    return 0

def generateNextInput(listOfNumbers):
    
    rand = random.randrange(0, 4, 1)
    print(rand)
    
    listOfNumbers.append(rand)
    
    return 0

def searchForPress(i, listOfNumbers):
    #blue
    
    button = 0
    win = 0
    
    while True:
        if GPIO.input(17):
            button = 17
            print("Pin 17 is HIGH")
            w = i % 100
            if w <= 50:
                GPIO.output(27, GPIO.HIGH)
            else:
                GPIO.output(27, GPIO.LOW)
            i = i + 1
                
        else:
            #print("Pin 17 is LOW")
            GPIO.output(27, GPIO.LOW)
                
            ##################################    

        #red

        if GPIO.input(5):
            button = 5
            print("Pin 5 is HIGH")
            w = i % 100
            if w <= 50:
                GPIO.output(6, GPIO.HIGH)
            else:
                GPIO.output(6, GPIO.LOW)
            i = i + 1
        else:
            #print("Pin 5 is LOW")
            GPIO.output(6, GPIO.LOW)
                
            ##################################    
                
        #yellow
                
        if GPIO.input(13):
            button = 13
            print("Pin 13 is HIGH")
            w = i % 100
            if w <= 50:
                GPIO.output(26, GPIO.HIGH)
            else:
                GPIO.output(26, GPIO.LOW)
            i = i + 1
        else:
            #print("Pin 13 is LOW")
            GPIO.output(26, GPIO.LOW)
                
            ##################################    
        #green        
        if GPIO.input(20):
            button = 20
            print("Pin 20 is HIGH")
            w = i % 100
            if w <= 50:
                GPIO.output(21, GPIO.HIGH)
            else:
                GPIO.output(21, GPIO.LOW)
            i = i + 1
        else:
            #print("Pin 20 is LOW")
            GPIO.output(21, GPIO.LOW)
            
        printButton(button, win, listOfNumbers)
        if(win == 1):
            break
            
    return 0

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

    i = 0
    x = 3
    buttonPressed = 0

    listOfNumbers = []

    random.seed(568)

    rand = random.randrange(0, 3, 1)
    
    while True:
        generateNextInput(listOfNumbers)
        printGeneratedNumbers(listOfNumbers)
        searchForPress(i, listOfNumbers)
    
    

main()
