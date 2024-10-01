import pyautogui
import keyboard
import time
valid = False
finished = False
pressed = False
decision = "null"
coinsFinal = 0
coinsInput = 0
pressTime = 0

# Should Use match and case!!!!!
# Should use import os
# Should use os.system("cls")


def CoinsValid(valid, cI, cF):

    if cI == 20:
        valid = True
        cF += cF
        coinsInput = 0
        return valid
    elif cI == 50:
        valid = True
        cF += cF
        cF = 0
        return valid
    elif cI == 100: 
        cF += cF
        cF = 0
        valid = True
        return valid
    elif cI != 20 & cI != 50 & cI != 100:
        valid = False
        print("Coin Not Accepted")
        return valid

def CoinInput(cI):
    cI = int(input("Enter a coin [20][50][100]"))
    return cI
    #if type(coinsInput) is int:
        #return coinsInput
    #else:
        #print("Fatal Error")



print("This machine accepts 50p coins 20p coins and 1 pound coins")

coinsInput = CoinInput(coinsInput)
print(coinsInput)


while finished != True:

    valid = CoinsValid(valid, coinsInput, coinsFinal)

    if coinsInput > 0:
        coinsInput = 0

    if valid == True:   
        print("Do you want to enter more coins. Press 'y' or 'n' on your keyboard")

        pressed == False

        while pressed == False:
            pressTime += 1
            if keyboard.is_pressed('y'):
                pressed = False
                pyautogui.press('backspace')
                coinsInput = CoinInput(coinsInput)
            elif keyboard.is_pressed('n'):
                pressed = False
                pyautogui.press('backspace')
                finished = False
            elif pressTime > 1000000000:
                print("Time Out")


print("has finished")








