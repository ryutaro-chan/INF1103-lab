inventory = 0
while True:
    userInput = input("Enter a stock quantity or type 'quit' to exit: ")
    if userInput == "quit":
        break
    if userInput.isdigit() == False:
        print("Please input a positive integer")
    else:
        inventory += int(userInput)
    if inventory > 500: 
        print ("Overstock") 
        break