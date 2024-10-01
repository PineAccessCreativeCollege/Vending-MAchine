import time

valid = False
finishedEntering = False
pressedButton = False
continueEnteringBool = True
continueEnteringStr = "Null"

coinsFinal = 0
coinInput = 0 
pressTime = 0

coinsAvailable = 1000
selectingItems = True
codeList = ["A01", "A02", "A03", "A04", "A05", "A06", "A07"]
#["Gravity control potion", "Milk and Cookies", "Chaos Guardian", "Burrito", "Cheese", "Necronomicon", "Radio"]
priceList = ["20", "50", "100", "170", "200", "250"]


boughtItems = []
#itemList = ["Gravity control potion", "Milk and Cookies", "Chaos Guardian", "Burrito", "Cheese", "Necronomicon", "Radio"]
finalItemList = []

valid = False
continueEntering = False
currentItem = "null"
currentItemName = "null"
currentItemPrice = 0
coinsPulled = 0

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
    cI = int(input("Enter a coin [20] [50] [100] "))
    return cI


while finishedEntering != True:
    

    if continueEnteringBool == True:

        coinInput = CoinInput()
        #print(coinInput)
        valid = CoinValidation(valid, coinInput, coinsFinal)
        #print(valid)

        if valid == True:
            coinsFinal += coinInput
            #print(coinsFinal)
        elif valid != True:
            coinsFinal += coinInput
            Terminator(coinsFinal)

        continueEnteringStr = str(input("Continue Entering [Y] or [N] "))
        if continueEnteringStr == "Y":
            #print("YES")
            continueEnteringBool = True
        elif continueEnteringStr == "N":
            #print("NO!!!")
            continueEnteringBool = False
            finishedEntering = True
        else:
            ("Error: Terminating")
            Terminator(coinsFinal)

    else:
        print("On to Item Selection")

    
    
print("""Items include: 
[Gravity control potion:  £0.20 A01]
[Milk and Cookies:        £0.50 A02]
[Chaos Guardian:          £1.00 A03]
[Burrito:                 £1.70 A04]
[Cheese:                  £2.00 A05]
[Necronomicon:            £2.50 A06]
[Radio:                   £2.50 A07]""")


def Terminator2(cP, cIP):
    print("Returning" + int(cP) + "coins!!!")
    
    
def ItemSelection(cI):
    cI = str(input("Enter an item code: "))
    return cI

def ItemValidator(cI, cL, valid):
    #timesCounted = 0
    hasRun = False
    #while hasRun == False:
        #for i in cL:
            #print("Running For")
            #timesCounted += 1
            #if cI == i:
                #print("if")
                #hasRun = True
                #valid = True
                #break
            #elif timesCounted > 8:
                #hasRun = True
                #valid = False
                #break
       
    if cI == "A01":
        valid = True
        return valid
    if cI == "A02":
        valid = True
        return valid
    if cI == "A03":
        valid = True
        return valid
    if cI == "A04":
        valid = True
        return valid
    if cI == "A05":
        valid = True
        return valid
    if cI == "A06":
        valid = True
        return valid
    if cI == "A07":
        valid = True
        return valid
    else:
        valid = False
        return valid 


def PricesCalculator(cI, pL):
    
    if cI == "A01":
        currentItemPrice = 20
        return currentItemPrice
    if cI == "A02":
        currentItemPrice = 50
        return currentItemPrice
    if cI == "A03":
        currentItemPrice = 100
        return currentItemPrice
    if cI == "A04":
        currentItemPrice = 170
        return currentItemPrice
    if cI == "A05":
        currentItemPrice = 200
        return currentItemPrice
    if cI == "A06":
        currentItemPrice = 250
        return currentItemPrice
    if cI == "A07":
        currentItemPrice = 250
        return currentItemPrice
    
def NameScanner(cL, cI):
    #for i in cL
    
    #for row in cL:
        #for element in row:
            #if cI == element:
                #element.index(cI)
    
    if cI == "A01":
        currentItemName = "Gravity control potion"
        return currentItemName
    if cI == "A02":
        currentItemName = "Milk and Cookies"
        return currentItemName
    if cI == "A03":
        currentItemName = "Chaos Guardian"
        return currentItemName
    if cI == "A04":
        currentItemName = "Burrito"
        return currentItemName
    if cI == "A05":
        currentItemName = "Cheese"
        return currentItemName
    if cI == "A06":
        currentItemName = "Necronomicon"
        return currentItemName
    if cI == "A07":
        currentItemName = "Radio"
        return currentItemName
    else:
        Terminator()

def ItemContinue():
    cont = str(input("Would you like to choose another item [Y] or [N] "))
    if cont == "Y":
        continueV = True
        return continueV
    elif cont == "N":
        continueV = False
        return continueV

while selectingItems != False:

    currentItem = ItemSelection(currentItem)
    valid = ItemValidator(currentItem, codeList, valid)
    
    if valid == True:
        currentItemPrice = PricesCalculator(currentItem, priceList)
        if coinsFinal >= currentItemPrice:
            coinsFinal -= currentItemPrice
            coinsPulled += currentItemPrice
            currentItemPrice = 0
            currentItemName = NameScanner(codeList, currentItem)
            boughtItems.append(currentItemName)
            #print("got through")
            continueEntering = ItemContinue()
        elif coinsFinal < currentItemPrice:
            print("No Funds")
            
    elif valid == False:
        print("Item Not Valid")
        boughtItems.clear()
        finalItemList.clear()
        Terminator2(coinsPulled, currentItemPrice)
        
    if continueEntering == True:
        selectingItems = True
    else:
        selectingItems = False
        


print("You bought" + str(boughtItems))
print("Your change is: " + str(coinsFinal) + " coins")