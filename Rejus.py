#Rejus Task 1
#Currency Converter

import time

#Global Single intialisation of value to accomodate for fluxuation
rates = [[1.00,1.30,1.20,143.23],
                 [0.77,1.00,0.92,109.78],
                 [0.83,1.08,1.00,118.91],
                 [0.0070,0.0091,0.0084,1.00]]

def exRates():
    #£1 = 1.20$, 1.30€ , 143¥

    #2d list housiing 16 conversion options
    visRates =[("£:£, £:$, £:€, £:¥"),
               ("$:£, $:$, $:€, $:¥"),
               ("€:£, €:$, €:€, €:¥"),
               ("¥:£, ¥:$, ¥:€, ¥:¥\n")]
    
    print ("Each list is ordered '£','$','€','¥'  :  Python automatically reduces redundant 0s.\n")
    for i in range(0,4):
        print (visRates[i])
    
    for i in range(0,4):
        print (rates[i])

    change = input("\nDo you wish to change any of these rates? Y:N")
    change = change.upper()
    if change == ("N"):
        print("\n\n\n")                
        hub()
    if change == ("Y"):
        print("\n\n\n")
        changeEx = input("Which currenices do you want to exchange, format : 'Y:X'  :\n  Where 0=£ , 1=$, 2=€, 3=¥")
        if changeEx != 0 or changeEx != 1 or changeEx != 2 or changeEx != 3:
            exRates()
    if change != "Y" and change != "N" :
        exRates()
        
        #Validation checks to make sure inputed location exists, if not restart
        for i in range(0,4):
            
            if int(changeEx[0:1]) == i:
                rateOne = int(changeEx[0:1])
                valid=1
                
                for j in range(0,4):
                    if int(changeEx[2:3]) == j:
                        valid=valid+1
                        rateTwo = int(changeEx[2:3])
                    elif valid <2 and j == 4:
                        print("\nInvalid")
                        time.sleep(1.25)
                        print("\n\n\n")  
                        exRates()
        #END OF validation checks
                        
        
        if valid == 2:
            validChange = input("\nTo what do you want to change the rate too? Must have 2 decimal places but no more.")
            revNum = validChange[::-1]
            if revNum[2:3] != ".":
                print("\nInvalid")
                time.sleep(1.25)
                print("\n\n\n")  
                exRates()
            else:
                rates[rateOne][rateTwo] = float(validChange)
                for i in range(0,4):
                    print (rates[i])
                time.sleep(1.25)
                print("\n\n\n")  
                exRates()
        
    return 0


def exchange(attained,wanted):

    amount = input("How much of your desired currency do you want, exchanged from your available currency?")
    rateExchange = rates[int(wanted)][int(attained)]
    newAmount = float(amount) * float(rateExchange)
    print (newAmount ,"currency will be required.") #Python rounds it, but answer is still valid to account for exchange fees            time.sleep(1.25)
    time.sleep(1.25)
    print("\n\n\n")  
    hub()

    return 0






def hub():  #Navigation center
    print ("...")
    action = input("Welcome to currency converter, do you want to:\n Exchange Currency:1 or View Rates:2 \n type the respective number")

    if action ==("1"):
        #Currencies declared out of appropiate subroutine so people dont have to restart their rates from scratch since a user isn't likely to suddenly change travel plans
        attained = input("\nWhat currency do you have? GBP(0),USD(1),EUR(2),JPY(3) using the respective number")
        attained = attained.upper()
        wanted = input("\nWhat currency do you want?")
        wanted = wanted.upper()
        print("\n\n\n")
        exchange(attained,wanted)
    
    if action == ("2"):
        print("\n\n\n")
        exRates()

    elif action != "1" and action != "2" :
         print("\nInvalid")
         time.sleep(1.25)
         print("\n\n\n")
         hub()
        
    return 0

hub()
