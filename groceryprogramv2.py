'''
Author: Ambrosio Gomez 2023

Welcome to my grocery Calculator program. 
I'm writing this program because it's usually quite a hassle to split groceries with my Room Mates because each one of them wants to split different things

With this program, you can go item per item, designating who's paying for and it'll do all the math for you
'''

# this creates the list that has everyone that can split groceries. I live with 4 roomates, so im inputting all of us into this
def listCreation():

    #establishes an empty dictionary, where names:amounts owed will be held
    whoOwesWhat = {}
    
    while True:
        
        #has the user type the names of who's splitting until they are finished
        print("Please enter their names one at a time. When you're done, press enter: ")
        while True:
            name = input().lower()
            if name == "":
                break
            else:
                #adds the name to the empty dictionary, with amount owed at 0
                whoOwesWhat.update({name:0})
        
        #lists out the names the user inputted, so they can make sure there's no user error
        print("So this is who's splitting the groceries? (check for any possible misspellings)")
        for key in whoOwesWhat:
            print(key)
        
        #has the user confirm their inputs, or restarts this part of the program 
        decision = input("Enter Y/N: ").lower()
        if decision == "y":
            print("Okay, that's who will be splitting the groceries. Let's find out how they are split on a per item basis. \n")
            break
        else:
            whoOwesWhat = {}
            print("Ok then, lets try again. ")
            
    #returns the dectionary with all the correct names in it        
    return whoOwesWhat

#creates a temporary dictionary to organize who's paying how much for a specific grocery item
def peopleList(whoOwesWhat):
    #whoOwesWhat is passed into this function, so we can reference it to see if the names entered here were established earlier
    
    #creates the empty temp dictionary
    peoplePerGrocery = {}
    
    #keeps asking for names until the user presses enter
    while True:
        
            #asks the user for the name
            print("Who's splitting: ")
            name = input().lower()
            
            #lets the user exit this part of the program, returns the temporary dictionary
            #contains name:amountOwed for this specific grocery item. amountOwed is still equal to 0 as of now
            if name == "":
                return peoplePerGrocery
            
            #if the user types all, will automatically evenly split the grocery price amongst the amount of people they entered and returns the dictionary
            elif name == "all":
                for name in whoOwesWhat:
                    peoplePerGrocery.update({name:0})
                return peoplePerGrocery
            #if the name entered is not in the original list, user is prompted with an error message
            elif name not in whoOwesWhat:
                print("That name is not in the list. Please check for any possible misspellings")
            #finally, if the user enters an acceptable name, the temp dictionary is updated with amountOwed = 0
            else:
                peoplePerGrocery.update({name:0})

#this function does the math, distributes the price of each grocery onto each person, then adds what they owe to their grand sum
def groceryCalculations(whoOwesWhat):
    #this is the total of everyone's groceries, so u can make sure what you've entered was accurate
    groceryTotal = 0
    
    print("Please input who's splitting the grocery item one at a time. If everyone's splitting, type 'all'. Press enter to finish.")
    
    #runs until the user types STOP
    while True:  
        
        #creates a temporary dictionary that splits the price of the grocery by how many people are paying for it
        #we pass the whoOwesWhat dictionary as an argument so we can reference the names in that list
        tempDict = peopleList(whoOwesWhat)
        #gets the amount of people paying for one grocery, so we can divide the cost evenly between them
        peopleCounter = len(tempDict)
        
        #asks the user to input the grocery cost as a float, gives them an error message if another data type is recieved
        while True:
            try:
                groceryValue = float(input("How much did the grocery cost? "))
                break
            except ValueError:
                print("That is not a grocery amount. Pleaes try again. ")

        #adds the cost of the grocery to the grand total
        groceryTotal += groceryValue
    
        #adds the appropriate amount to each person in the whoOwesWhat dictionary
        #the amount is the grocery cost/how many people paid for it
        for name in tempDict:
            whoOwesWhat.update({name:whoOwesWhat[name] + (groceryValue/peopleCounter)})
        
        #asks user if they want to continue using the program
        userContinue = input("Grocery submitted. Do you want to continue? (Type STOP to end the program, enter anything else to continue. )").lower()
        if userContinue == "stop":
            break
    
    #prints how much each person owes
    for name in whoOwesWhat:
        print(f"{name} owes ${whoOwesWhat[name]:.2f}")
       
    #prints the grand total 
    print(f"The total amount is ${groceryTotal:.2f}")
                   
if __name__ == "__main__":
    print("GROCERY CALCULATOR!!!! Split your grocery costs with your roomates. ")
    
    #has user create a dictionary with everyone who is going to pay something
    whoOwesWhat = listCreation()
    
    #passes this dictionary to the groceryCalculations function, that will calculate how much they owe
    groceryCalculations(whoOwesWhat)
    