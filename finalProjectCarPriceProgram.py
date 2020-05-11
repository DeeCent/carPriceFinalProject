"""
    Final Exam  Car Price Program
     4.20.20
    Purpose: Calculate car price based on choices
"""

basePrice = 0.0         #Define global variables
engineCost = 0.0
trimCost = 0.0
radioCost = 0.0
carMake = ""
SHIPPINGCHARGE = 500    #Define global CONSTANTS
DEALERCHARGE = 175
    
def main():
    global basePrice, carMake

    yourName = input("What is your name? ") #Declares yourName as local variable.
                                            #Local variables can only be used in the function they were created.
 
    print("\nWelcome " + yourName + ", to the vehicle cost calculator.\n" \
          "Please follow on screen instructions.\n") #Welcome message

    carMake = input("please choose the make of the vehicle you are looing for? choose one of following: Dodge, Chevy, Ford, Chevrolet." ) 
    
    basePrice = float(input("What is the base price of the " + carMake + " you are looking to buy? "))

    engineCostMod() #Calling all our modules
    trimCostMod()
    radioCostMod()
    sellingPriceMod()


def engineCostMod():    #Determines the engine cost by user input
    global engineCost

    engineChoice = ''   #Declares engineChoice as local variable

    #Displays selection choices
    engineChoice = input("\nPlease select one of the choices by \n" \
                       "using the designated letter.\n" \
                       "S - 6 cylinder engine.\n" \
                       "E - 8 cylinder engine.\n" \
                       "D - Diesel Engine.\n" \
                       "Selection: ")
    
    if engineChoice == 's' or engineChoice == 'S':
        engineCost = 150
        
    elif engineChoice == 'e' or engineChoice == 'E':
        engineCost = 475
        
    elif engineChoice == 'd' or engineChoice == 'D':
        engineCost = 750
        
    else:
        print("\nInvalid selection!\n") #Defensive catch, recalls this module to restart.
        engineCostMod()

def trimCostMod():  #Determines the trim cost by user input
    global trimCost

    trimChoice = '' #Declares trimChoice as local variable

    #Displays selection choices
    trimChoice = input("\nPlease select one of the choices by \n" \
                       "using the designated letter.\n" \
                       "V - Vinyl interior trim.\n" \
                       "C - Cloth interior trim.\n" \
                       "L - Leather interior trim.\n" \
                       "Selection: ")
    
    if trimChoice == 'v' or trimChoice == 'V':
        trimCost = 50

    elif trimChoice == 'c' or trimChoice == 'C':
        trimCost = 225

    elif trimChoice == 'l' or trimChoice == 'L':
        trimCost = 800

    else:
        print("\nInvalid Selection!\n") #Defensive catch, recalls this module to restart.
        trimCostMod()

def radioCostMod(): #Determines the radio cost by user input
    global radioCost

    radioChoice = ''    #Declares radioChoice as local variable

    #Displays selection choices
    radioChoice = input("\nPlease select one of the choices by \n" \
                       "using the designated letter.\n" \
                       "R - AM/FM/CD/DVD.\n" \
                       "G - with GPS.\n" \
                       "Selection: ")

    if radioChoice == 'r' or radioChoice == 'R':
        radioCost = 100

    elif radioChoice == 'g' or radioChoice == 'G':
        radioCost = 400

    else:
        print("\nInvalid Selection!")   #Defensive catch, recalls this module to restart.
        radioCostMod()

def sellingPriceMod():  #Calculates and prints total cost of the vehicle
    global SHIPPINGCHARGE, DEALERCHARGE, carMake

    sellingPrice = 0.0  #Declares sellingPrice as local variable

    sellingPrice = basePrice + engineCost + trimCost + radioCost + SHIPPINGCHARGE + DEALERCHARGE    #Calculates total cost

    print("\nThe total price for your " + carMake + " is $" + str(sellingPrice))    #Prints total cost

    print("\nWould you like to buy another car?")
    
main()  #Calling the main module
                      
                    
        
    
