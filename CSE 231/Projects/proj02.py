###############################################################################
#  Computer Project #2
#  
# prompt for a cost (str)
# loop while str is not q 
#    calculate value of total change    
#    convert cost str to float and multiply by 100 then convert to an int
#    if cost is negative
#       display an error message
#       re-prompt cost
#    prompt for payment
#    if payment is less than cost
#       display an error message
#       re-prompt payment
#    if payment is equal to cost 
#       display "No change."
#       restart loop
#    calculate difference of payment and cost 
#    if difference is greater than value of total change
#       display an error message and quit
#    use a while loop to subtract coin value from difference 
#       Iterate through coins, decrementing the stock & incrementing the change
#    display coins dispense
#    reprompt user for a cost
###############################################################################

# Stock of coins
quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("Welcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

while in_str != 'q':
    
    # Calculates total value of change in stock
    total_change = quarters*25+dimes*10+nickels*5+pennies
    
    # Sets change dispensed values to 0 
    quarter_change = 0
    dime_change = 0
    nickel_change = 0
    penny_change = 0

    # Converts str input to float then multiplies it by 100 and converts to int
    # This is done to avoid impersision during calculations involving cents
    cost = int(float(in_str)*100) 
    
    if cost < 0: # Checks if cost is negative
        print("\nError: purchase price must be non-negative.")
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
              .format(quarters, dimes, nickels, pennies))
        in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
        continue # Restarts loop
    
    # Converts payment str input to int and multiplies it by 100
    payment = int(input("\nInput dollars paid (int): "))*100 
    
    while cost > payment: # Checks for insufficent payment
        print("\nError: insufficient payment.")
        # Converts payment str input to int and multiplies it by 100
        payment = int(input("\nInput dollars paid (int): "))*100
    
    if cost == payment: # Checks if no change is needed
        print("\nNo change.")
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
              .format(quarters, dimes, nickels, pennies))
        in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
        continue # Restarts loop
    
    diff = payment - cost # Calculates the difference of payment and cost 
    
    if diff > total_change: #Checks if difference > value of coin stock
        print("\nError: ran out of coins.")
        break # Halts program
    
    # Loop continues to dispense change until balance owed is 0
    while diff > 0: 
        if diff >= 25:
            # Ends when change due is less than a quarter's value or if
            # quarter stock is 0
            while diff >= 25 and quarters > 0:
                quarters -= 1 # Decreases quarter stock
                quarter_change += 1 # Increases quarters dispensed count
                diff -= 25 # Subtracts a quarter's value from change owed
                
        if diff >= 10:
            # Ends when change due is less than a dime's value or if 
            # dime's stock is 0
            while diff >= 10 and dimes > 0:
                dimes -= 1 # Decreases dime stock
                dime_change += 1 # Increases dimes dispensed count
                diff -= 10 # Subtracts dime value from change owed
                
        if diff >= 5:
            # Ends when change due is less than a nickel's value or if
            # nickel stock is 0
            while diff >= 5 and nickels > 0:
                nickels -= 1 # Decreases nickel stock
                nickel_change +=1 # Increases nickels dispensed count
                diff -= 5 # Subtracts a nickel's value from change owed
                
        if diff >= 1:
            # Ends when change due is less than a penny's value or if
            # penny stock is 0
            while diff >= 1 and pennies > 0:
                pennies -= 1 # Decreases penny stock
                penny_change += 1 # Increases pennies dispensed count
                diff -= 1 # Subtracts a penny's value from change owed
    
    # Prints out change dispensed for each coin used to repay customer 
    print("\nCollect change below: ")
    if quarter_change > 0: 
        print("Quarters: {}".format(quarter_change))
    if dime_change > 0:
        print("Dimes: {}".format(dime_change))
    if nickel_change > 0:
        print("Nickels: {}".format(nickel_change))
    if penny_change > 0:
        print("Pennies: {}".format(penny_change))
        
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")