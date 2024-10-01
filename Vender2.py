import time

valid = False
finishedEntering = False
pressedButton = False
continueEnteringBool = True
continueEnteringStr = "Null"

coinsFinal = 0
coinInput = 0 
pressTime = 0


def Terminator(cF):
    print("Returning " + str(cF) + " coins to user")

def CoinValidation(valid, cI, cF):

    if cI == 20:
        valid = True
        cF += cI
        return valid
    elif cI == 50:
        valid = True
        cF+=cI
        return valid
    elif cI == 100:
        valid = True
        cF+=cI
        return valid
    elif cI != 20 & cI !=50 & cI != 100:
        valid = False
        print("Coin not accepted")
        return valid



def CoinInput():
    cI = int(input("Enter a coin [20] [50] [100]"))
    return cI


while finishedEntering != True:
    

    if continueEnteringBool == True:

        coinInput = CoinInput()
        print(coinInput)
        valid = CoinValidation(valid, coinInput, coinsFinal)
        print(valid)

        if valid == True:
            coinsFinal += coinInput
            print(coinsFinal)
        elif valid != True:
            coinsFinal += coinInput
            Terminator(coinsFinal)

        continueEnteringStr = str(input("Continue Entering 'Y' or 'N'"))
        if continueEnteringStr == "Y":
            print("YES")
            continueEnteringBool = True
        elif continueEnteringStr == "N":
            print("NO!!!")
            continueEnteringBool = False
            finishedEntering = True
        else:
            ("Error: Terminating")
            Terminator(coinsFinal)

    else:
        print("On to Item Selection")

    