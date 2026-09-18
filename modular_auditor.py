inventory = 0
Rejected = 0
total_deliveries = 0
total_tax = 0.0
TAX_RATE = 0.1

while True:
    userInput = input("Enter a stock quantity or type 'quit' to exit: ")
    
    if userInput == "quit":
        print("Total Deliveries Processed: " + str(total_deliveries))
        print("Total Units Processed: " + str(inventory))
        print("Total Tax: $" + str(round(total_tax, 2)))
        print("Number of Failed/Rejected: " + str(Rejected))
        break
        
    elif userInput.isdigit() == False:
        Rejected += 1
        print("Please input a positive integer")
        
    else:
        delivery_amount = int(userInput)
        
        inventory += delivery_amount
        total_deliveries += 1
        
        delivery_tax = delivery_amount * TAX_RATE
        total_tax += delivery_tax
        
    if inventory > 500:
        print("Overstock")
        break
           