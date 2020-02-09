
import random


randomNumber = int()
closeVar = int()
iterator = int()
digit = int()
numbersListLen = int()
userNum = int()
random.seed(0)

numbersList = []
letterList = []

closeVar = 0
iterator = 0



while(closeVar == 0):
	randomNumber = random.randrange(1,4,1)
	numbersList.append(randomNumber)
	numbersListLen = len(numbersList)
	digit = iterator + 1
	iterator = 0

	#prints out memory list
	while( iterator < numbersListLen ):
		print(numbersList[iterator])
		iterator = iterator + 1
		continue
	
	iterator = 0

	#asks for user input and checks user input
	while( iterator < numbersListLen ):
		print('Enter number ',digit)
		userNum = input()

		if(userNum != numbersList[iterator]):
			closeVar == 1
			break

		iterator = iterator + 1
		continue
	continue
