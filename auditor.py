inventory = 0
Rejected = 0
while True:
    userInput = input("Enter a stock quantity or type 'quit' to exit: ")
    if userInput == "quit":
        print("Total Units Processed" + str(inventory))
        print("Number of Failed/Rejected"+ str(Rejected)) 
        break
    elif userInput.isdigit() == False:
        Rejected += 1
        print("Please input a positive integer")
    else:
        inventory += int(userInput)
    if inventory > 500: 
        print ("Overstock") 
        break
           