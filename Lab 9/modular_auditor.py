def get_valid_input():
    """Prompts for input and validates whether it's a positive integer or 'quit'."""
    user_input = input("Enter a stock quantity or type 'quit' to exit: ")
    
    if user_input == "quit":
        return "quit"
    elif user_input.isdigit():
        return int(user_input)
    else:
        print("Please input a positive integer")
        return None


def process_delivery(current_total, new_value):
    """Calculates and returns the new running total."""
    return current_total + new_value


def calculate_tax(amount):
    """Calculates and returns a 10% tax for a given delivery amount."""
    return amount * 0.10


def generate_report(total_units, failed_attempts, total_tax):
    """Prints the final summary report."""
    print("Total Units Processed: " + str(total_units))
    print("Total Tax: $" + str(round(total_tax, 2)))
    print("Number of Failed/Rejected: " + str(failed_attempts))


def main():
    inventory = 0
    rejected = 0
    total_tax = 0.0

    while True:
        result = get_valid_input()

        if result == "quit":
            generate_report(inventory, rejected, total_tax)
            break
        elif result is None:
            rejected += 1
        else:
            inventory = process_delivery(inventory, result)
            
            tax = calculate_tax(result)
            total_tax += tax
            
            print("Tax for this delivery: $" + str(tax))
            
        if inventory > 500:
            print("Overstock")
            break


main()